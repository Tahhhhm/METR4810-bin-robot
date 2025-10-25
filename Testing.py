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

BIN_THRESHOLD = 400
ROAD_THRESHOLD = 350
#ENDING = 10000

bin_aligned = False
off_road_left = False
off_road_right = False
bin_location = None
next_road = None
tile_list = ["straight"]  # First action is always a straight line
tile_action_paused = False
distance = None
obstacle = False
#Tile_end = False

# ---------------------- Hardware setup ----------------------
motor_assembly = MOTOR_CODE.Motor(20, 16, 26, 19, 21, 13)
#colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
# ultrasonic = ULTRASONIC_CODE.ObstacleDetector(trigger_pin=5, echo_pin=6)
# camera = Detection.AI()


# ---------------------- Sensor listener ----------------------
def sensor_listener():
    global bin_aligned, bin_location, distance, off_road_left, off_road_right, obstacle

    while True:
        if not program_running:
            break

        # Read color sensor data
        left_road_csensor = colour_sensor2.readRGB()
        right_road_csensor = colour_sensor4.readRGB()

        # Read ultrasonic distance
        #distance = ultrasonic.obstacle_distance()

        # Off-road detection
        off_road_left = left_road_csensor['green'] > ROAD_THRESHOLD 
        off_road_right = right_road_csensor['green'] > ROAD_THRESHOLD

        # Tile end detection
        # Tile_end = left_road_csensor > ENDING and right_road_csensor > ENDING

        # Obstacle detection
        # obstacle = distance <= 8

        # Bin alignment
        #if left_bin_csensor >= BIN_THRESHOLD:
        #    bin_aligned = True
        #    bin_location = "left"
        #if right_bin_csensor >= BIN_THRESHOLD:
        #    bin_aligned = True
        #    bin_location = "right"
        #else:
        #    bin_aligned = False
        #    bin_location = None

        time.sleep(0.5)

# ---------------------- Input listener ----------------------
def input_listener():
    global current_mode, switch_requested, program_running
    while True:
        user_input = input("\n(Type 'switch <mode>' or 'exit'): ").strip().lower()
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

# ---------------------- Robot modes ----------------------
def idle_mode():
    print("[IDLE MODE] Running...")
    while True:
        if switch_requested or not program_running:
            break
        #motor_assembly.forward()
        # if off_road_right and off_road_left:
        #     print("stopping...")
        # elif off_road_right:
        #     print("need to turn left")
        # elif off_road_left:
        #     print("need to turn right")
        # else:
        #     print("onward")
        
def start_mode():
    global bin_aligned, next_road, tile_action_paused
    print("[START MODE] Running...")
    motor_assembly.set_speed(60)

    while True:
        if switch_requested or not program_running:
            break
        
        motor_assembly.stop()
        print(f"[DEBUG] obstacle={obstacle}, off_road_left={off_road_left}, off_road_right={off_road_right}, bin_aligned={bin_aligned}")

        # --- 1. Obstacle avoidance ---
        if obstacle:
            print("[AVOIDANCE] Obstacle detected! Stopping...")
            motor_assembly.stop()
            sleep_ms(5)
            continue

        # --- 2. Off-road recovery ---
        elif off_road_left and off_road_right:
            print("[CORRECTION] Both sensors off-road. Stopping...")
            motor_assembly.stop()
            sleep_ms(5)
            continue

        elif off_road_right:
            print("[CORRECTION] Off-road (right). Turning left...")
            motor_assembly.turn_left()
            sleep_ms(5)
            continue

        elif off_road_left:
            print("[CORRECTION] Off-road (left). Turning right...")
            motor_assembly.turn_right()
            sleep_ms(5)
            continue

        # --- 3. Bin handling ---
        elif bin_aligned:
            print("Bin ready in position")
            motor_assembly.stop()
            if bin_location == "left":
                ServoController.pickup_left()
            elif bin_location == "right":
                ServoController.pickup_right()
            bin_aligned = False
            sleep_ms(5)
            continue

        # --- 4. Default movement ---
        else:
            print("Nothing stopping me, going forward...")
            motor_assembly.forward()
        
        sleep_ms(5)


def return_mode():
    print("[RETURN MODE] Running...")
    while True:
        if switch_requested or not program_running:
            break
        motor_assembly.backward()
        time.sleep(1)
        motor_assembly.stop()

def stop_mode():
    print("[STOP MODE] Running...")
    while True:
        if switch_requested or not program_running:
            break
        motor_assembly.stop()
        time.sleep(0.1)

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

    while True:
        if not program_running:
            motor_assembly.stop()
            break
        mode_function = modes.get(current_mode, idle_mode)
        switch_requested = False

        mode_function()
        print(f">>> Switching mode to '{current_mode}'...\n")


    motor_assembly.stop()
    print("Program exited.")

# ---------------------- Run main ----------------------
if __name__ == "__main__":
    main()
