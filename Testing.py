import Colour_sensor
import ULTRASONIC_CODE
import MOTOR_CODE
import threading
import time
import Detection
from PiicoDev_Unified import sleep_ms
from servo_testworking import pickup_bin
import traceback

# ---------------------- Global variables ----------------------
current_mode = "idle"
switch_requested = False
program_running = True

REDBIN_THRESHOLD = 2000 #red value
YELLOWBIN_THRESHOLD = 1850 #green value
LEFT_ROAD_THRESHOLD = 600
RIGHT_ROAD_THRESHOLD = 600
LEFT_OBSTACLE = 600 #blue value
RIGHT_OBSTACLE = 800 #blue value 
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
colour_sensor3 = Colour_sensor.ColourSensor(channel=4)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
# camera = Detection.AI()


# ---------------------- Sensor listener ----------------------
def sensor_listener():
    global bin_aligned, bin_location, distance, off_road_left, off_road_right, obst_left, obst_right, yellowbin, redbin

    while True:
        if not program_running:
            break

        # Read color sensor data
        left_road_csensor = colour_sensor2.readRGB()
        right_road_csensor = colour_sensor4.readRGB()
        right_bin_csensor = colour_sensor3.readRGB()

    

        # Off-road detection
        off_road_left = left_road_csensor['green'] > LEFT_ROAD_THRESHOLD 
        off_road_right = right_road_csensor['green'] > RIGHT_ROAD_THRESHOLD
        obst_left = left_road_csensor['red'] > LEFT_OBSTACLE
        obst_right = left_road_csensor['red'] > RIGHT_OBSTACLE
        yellowbin = right_bin_csensor['green'] > YELLOWBIN_THRESHOLD
        redbin = right_bin_csensor['red'] > REDBIN_THRESHOLD

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
        
def start_mode():
    global bin_aligned, next_road, tile_action_paused
    print("[START MODE] Running...")
    motor_assembly.set_speed(30)

    while True:
        if switch_requested or not program_running:
            break
        
        motor_assembly.stop()
        print(f"[DEBUG] obstacle={obstacle}, off_road_left={off_road_left}, off_road_right={off_road_right}, bin_aligned={bin_aligned}")

        # --- 1. Obstacle avoidance ---
        if obst_left:
            print("[AVOIDANCE] Left Obstacle detected! Stopping...")
            motor_assembly.turn_right()
            sleep_ms(10)
            continue
        
        elif obst_right:
            print("[AVOIDANCE] Right Obstacle detected! Stopping...")
            motor_assembly.turn_left()
            sleep_ms(10)
            continue

        # --- 2. Off-road recovery ---
        elif off_road_left and off_road_right:
            print("[CORRECTION] Both sensors off-road. Stopping...")
            motor_assembly.backward()
            sleep_ms(2)
            continue

        elif off_road_right:
            print("[CORRECTION] Off-road (right). Turning left...")
            motor_assembly.turn_left()
            sleep_ms(2)
            continue

        elif off_road_left:
            print("[CORRECTION] Off-road (left). Turning right...")
            motor_assembly.turn_right()
            sleep_ms(2)
            continue

        # --- 3. Bin handling ---
        elif yellowbin:
            motor_assembly.stop()
            print("Yellow Bin ready in position")
            pickup_bin()
            continue

        elif redbin:
            motor_assembly.stop()
            print("Red Bin ready in position")
            pickup_bin()
            continue

        # --- 4. Default movement ---
        else:
            print("Nothing stopping me, going forward...")
            motor_assembly.forward()
            sleep_ms(3)


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
