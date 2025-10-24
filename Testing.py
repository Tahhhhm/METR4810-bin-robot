import Colour_sensor
import ULTRASONIC_CODE
import MOTOR_CODE
import threading
import time
import Detection
from PiicoDev_Unified import sleep_ms
from SERVO_CODE import ServoController
import traceback

# ---------------------- Global variables ----------------------
current_mode = "idle"
switch_requested = False
program_running = True

GREEN_THRESHOLD = 400
ROAD_THRESHOLD = 250
ENDING = 10000

bin_aligned = False
off_road_left = False
off_road_right = False
bin_location = None
next_road = None
tile_list = ["straight"]  # First action is always a straight line
tile_action_paused = False
distance = None
obstacle = False
Tile_end = False

# Lock for thread-safe access
data_lock = threading.Lock()

# ---------------------- Hardware setup ----------------------
motor_assembly = MOTOR_CODE.Motor(17, 27, 22, 23, 24, 18)
colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
ultrasonic = ULTRASONIC_CODE.ObstacleDetector(trigger_pin=5, echo_pin=6)
camera = Detection.AI()

# ---------------------- Sensor listener ----------------------
def sensor_listener():
    global bin_aligned, bin_location, distance, off_road_left, off_road_right, Tile_end, obstacle
    try:
        while True:
            with data_lock:
                if not program_running:
                    break

                # Read color sensors
                left_bin_csensor = colour_sensor1.readRGB()['green']
                right_bin_csensor = colour_sensor2.readRGB()['green']
                left_road_csensor = colour_sensor3.readRGB()['green']
                right_road_csensor = colour_sensor4.readRGB()['green']

                # Read ultrasonic distance
                distance = ultrasonic.obstacle_distance()

                # Off-road detection
                off_road_left = left_road_csensor > ROAD_THRESHOLD
                off_road_right = right_road_csensor > ROAD_THRESHOLD

                # Tile end detection
                Tile_end = left_road_csensor > ENDING and right_road_csensor > ENDING

                # Obstacle detection
                obstacle = distance <= 8

                # Bin alignment
                if left_bin_csensor >= GREEN_THRESHOLD:
                    bin_aligned = True
                    bin_location = "left"
                elif right_bin_csensor >= GREEN_THRESHOLD:
                    bin_aligned = True
                    bin_location = "right"
                else:
                    bin_aligned = False
                    bin_location = None

            time.sleep(0.5)
    except Exception as e:
        motor_assembly.stop()
        print("[ERROR] Sensor listener crashed:", e)
        traceback.print_exc()

# ---------------------- Input listener ----------------------
def input_listener():
    global current_mode, switch_requested, program_running
    try:
        while True:
            user_input = input("\n(Type 'switch <mode>' or 'exit'): ").strip().lower()
            with data_lock:
                if not program_running:
                    break

                if user_input.startswith("switch"):
                    parts = user_input.split()
                    if len(parts) == 2:
                        current_mode = parts[1]
                        switch_requested = True
                    else:
                        print("Usage: switch <mode>")
                elif user_input == "exit":
                    program_running = False
                    switch_requested = True
                    print("Exiting program...")
    except Exception as e:
        motor_assembly.stop()
        print("[ERROR] Input listener crashed:", e)
        traceback.print_exc()

# ---------------------- Robot modes ----------------------
def idle_mode():
    try:
        print("[IDLE MODE] Running...")
        while True:
            with data_lock:
                if switch_requested or not program_running:
                    break
            time.sleep(1)
    except Exception as e:
        motor_assembly.stop()
        print("[ERROR] Idle mode crashed:", e)
        traceback.print_exc()

def start_mode():
    global bin_aligned, next_road, tile_action_paused
    try:
        print("[START MODE] Running...")

        # Start tile execution thread
        tile_thread = threading.Thread(target=motor_assembly.processTiles, args=(tile_list,), daemon=True)
        tile_thread.start()

        while True:
            with data_lock:
                if switch_requested or not program_running:
                    break

                local_obstacle = obstacle
                local_off_road_left = off_road_left
                local_off_road_right = off_road_right
                local_bin_aligned = bin_aligned
                local_bin_location = bin_location
                local_Tile_end = Tile_end

            # --- 1. Obstacle avoidance ---
            if local_obstacle:
                tile_action_paused = True
                print("[AVOIDANCE] Obstacle detected! Backing up...")
                motor_assembly.stop()
                time.sleep(0.2)

                motor_assembly.backward()
                time.sleep(1.0)
                motor_assembly.stop()
                time.sleep(0.2)

                print("[AVOIDANCE] Turning to avoid obstacle...")
                distance_log = []
                CLEAR_THRESHOLD = 20
                HISTORY_SIZE = 5
                TURN_TIMEOUT = 5.0
                TURN_DIRECTION = "left"

                if TURN_DIRECTION == "left":
                    motor_assembly.turn_left()
                    opposite_sensor = lambda: off_road_right
                else:
                    motor_assembly.turn_right()
                    opposite_sensor = lambda: off_road_left

                turn_start = time.time()
                while (time.time() - turn_start) < TURN_TIMEOUT:
                    d = ultrasonic.obstacle_distance()
                    distance_log.append(d)
                    if len(distance_log) > HISTORY_SIZE:
                        distance_log.pop(0)

                    if len(distance_log) == HISTORY_SIZE and all(x >= CLEAR_THRESHOLD or x == float('inf') for x in distance_log):
                        print("[AVOIDANCE] Path appears clear.")
                        break

                    if opposite_sensor():
                        print("[AVOIDANCE] Off-road detected — stopping turn.")
                        break

                    time.sleep(0.1)

                motor_assembly.stop()
                time.sleep(0.2)
                print("[AVOIDANCE] Resuming tile sequence.")
                tile_action_paused = False
                continue

            # --- 2. Off-road recovery ---
            elif local_off_road_left:
                tile_action_paused = True
                print("[CORRECTION] Off-road (left). Turning right...")
                motor_assembly.turn_right()
                time.sleep(0.5)
                motor_assembly.stop()
                tile_action_paused = False

            elif local_off_road_right:
                tile_action_paused = True
                print("[CORRECTION] Off-road (right). Turning left...")
                motor_assembly.turn_left()
                time.sleep(0.5)
                motor_assembly.stop()
                tile_action_paused = False

            # --- 3. Bin handling ---
            elif local_bin_aligned:
                tile_action_paused = True
                motor_assembly.stop()
                time.sleep(0.5)
                if local_bin_location == "left":
                    print("[BIN] Picking up bin on the left")
                    ServoController.pickup_left()
                elif local_bin_location == "right":
                    print("[BIN] Picking up bin on the right")
                    ServoController.pickup_right()
                motor_assembly.stop()
                time.sleep(0.5)

                with data_lock:
                    bin_aligned = False
                tile_action_paused = False

            # --- 4. Tile end handling ---
            elif local_Tile_end:
                tile_action_paused = True
                motor_assembly.stop()
                sleep_ms(500)

                next_tile = camera.detect_road()
                with data_lock:
                    tile_list.append(next_tile)
                    Tile_end = False
                print(f"[TILE] Detected next tile: {next_tile}")
                tile_action_paused = False

            time.sleep(0.1)

    except Exception as e:
        motor_assembly.stop()
        print("[ERROR] Start mode crashed:", e)
        traceback.print_exc()

def return_mode():
    try:
        print("[RETURN MODE] Running...")
        while True:
            with data_lock:
                if switch_requested or not program_running:
                    break
            motor_assembly.backward()
            time.sleep(1)
            motor_assembly.stop()
    except Exception as e:
        motor_assembly.stop()
        print("[ERROR] Return mode crashed:", e)
        traceback.print_exc()

def stop_mode():
    try:
        print("[STOP MODE] Running...")
        while True:
            with data_lock:
                if switch_requested or not program_running:
                    break
            motor_assembly.stop()
            time.sleep(0.1)
    except Exception as e:
        motor_assembly.stop()
        print("[ERROR] Stop mode crashed:", e)
        traceback.print_exc()

# ---------------------- Main ----------------------
def main():
    modes = {
        "idle": idle_mode,
        "start": start_mode,
        "return": return_mode,
        "stop": stop_mode
    }

    # Start listener threads
    threading.Thread(target=input_listener, daemon=True).start()
    threading.Thread(target=sensor_listener, daemon=True).start()

    global switch_requested

    try:
        while True:
            with data_lock:
                if not program_running:
                    break
                mode_function = modes.get(current_mode, idle_mode)
                switch_requested = False

            mode_function()
            print(f">>> Switching mode to '{current_mode}'...\n")

    except Exception as e:
        motor_assembly.stop()
        print("[ERROR] Main loop crashed:", e)
        traceback.print_exc()

    motor_assembly.stop()
    print("Program exited.")

# ---------------------- Run main ----------------------
if __name__ == "__main__":
    main()
