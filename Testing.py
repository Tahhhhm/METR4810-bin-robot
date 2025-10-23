import Colour_sensor 
import ULTRASONIC_CODE
import MOTOR_CODE
import threading
import time
import Detection
from PiicoDev_Unified import sleep_ms
from SERVO_CODE import ServoController
current_mode = "idle"
switch_requested = False
program_running = True
GREEN_THRESHOLD = 400 
bin_aligned = False
off_road_left = None
off_road_right = None
bin_location = None
next_road = None
distance = None
ROAD_THRESHOLD = 250


motor_assembly = MOTOR_CODE.Motor(17, 27, 22, 23, 24, 18)
colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
ultrasonic = ULTRASONIC_CODE.ObstacleDetector(trigger_pin=23, echo_pin=24)
camera=Detection.AI()


def listener():
    """
    Continuously monitors the color sensors to detect bin alignment.
    Continously monitors if the robot is off-road by ultrasonic
    Updates the global variable `bin_aligned` based on sensor readings.
    """
    global bin_aligned , bin_location, program_running, distance
    while program_running:
        rgbL = colour_sensor1.readRGB() # Left sensor bins 
        rgbR = colour_sensor2.readRGB() # Right sensor bins
        roadL = colour_sensor3.readRGB() # Left Front robot sensor
        roadR = colour_sensor4.readRGB() # Right Front robot sensor
        distance = ultrasonic.obstacles_present() # Detects front obstacles
        green_valueL = rgbL['green'] 
        green_valueR = rgbR['green']
        
        if roadL > ROAD_THRESHOLD:
            off_road_left = True
        else:
            off_road_left = False
        if roadR > ROAD_THRESHOLD:
            off_road_right = True
        else:
            off_road_right = False    
        if distance <= 3:
            obstacles = True
        else:
            obstacles = False   
        if green_valueL >= GREEN_THRESHOLD:
            bin_aligned = True
            bin_location = "left"
        elif green_valueR >= GREEN_THRESHOLD:
            bin_aligned = True
            bin_location = "right"
        else:
            bin_aligned = False
            bin_location = None
        time.sleep(0.5)  # Polling interval

def input_listener():
    """
    Runs in a separate thread to listen for mode change or exit requests.
    """
    global current_mode, switch_requested, program_running
    while program_running:
        user_input = input("\n(Type 'switch (idle, start, stop, return)").strip().lower()
        if user_input.startswith("switch"):
            parts = user_input.split()
            if len(parts) == 2:
                current_mode = parts[1]
                switch_requested = True
            else:
                print("Usage: switch <mode>")
        elif user_input == "exit":
            program_running = False
            switch_requested = True  # To break current mode loop


def idle_mode():
    print("[IDLE MODE] Running... (type 'switch <mode>')")
    while not switch_requested and program_running:
        time.sleep(1)  # Simulate background idle behavior

def start_mode():
    print('starting...')
    global bin_aligned next_road
    while not switch_requested and program_running:
        next_road=camera.detect_road()
        if off_road_left == True:
            motor_assembly.turn_right()
        else:
            motor_assembly.forward()
            sleep_ms(100)
        if off_road_right == True:
            motor_assembly.turn_left()
        else:
            motor_assembly.forward()
            sleep_ms(100)
        if bin_aligned == False:
            if next_road== 'straight'
            motor_assembly.forward()
            sleep_ms(2000)
            motor_assembly.forward()
            #how to explode map, and avoid things 
        elif bin_aligned == True:
             motor_assembly.stop()
             if bin_location == "left":
                print("Picking up bin on the left")
                #servo pickup code for left bin
                ServoController.pickup_left
             elif bin_location == "right":
                print("Picking up bin on the right")
                #servo pickup code for left bin

def return_mode():
    print("returning...")
    while not switch_requested and program_running:
        motor_assembly.backward()
        time.sleep(1)
        motor_assembly.stop()


def stop_mode():
    print("stopping...")
    while not switch_requested and program_running:
        motor_assembly.stop()


def main():
    # Function dictionary
    modes = {
        "idle": idle_mode,
        "start": start_mode,
        "stop": stop_mode,
        "return": return_mode
    }

    # Start the input listener in a separate thread
    listener_thread = threading.Thread(target=input_listener, daemon=True)
    listener_thread.start()
    
    colour_sensor_listener_thread = threading.Thread(target=listener, daemon=True)
    colour_sensor_listener_thread.start()


    global switch_requested

    while program_running:
        mode_function = modes.get(current_mode, idle_mode)
        switch_requested = False
        mode_function()  # Run the selected mode
        print(f">>> Switching mode to '{current_mode}'...\n")


    print("Program exited.")

if __name__ == "__main__":
    main()
import Colour_sensor 
import ULTRASONIC_CODE
import MOTOR_CODE
import threading
import time
import Detection
current_mode = "idle"
switch_requested = False
program_running = True
GREEN_THRESHOLD = 400 
bin_aligned = False
off_road = False
bin_location = None
next_road = None
tiles=["straight"]


motor_assembly = MOTOR_CODE.Motor(17, 27, 22, 23, 24, 18)
colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
#colour_sensor3 = Colour_sensor.ColourSensor(channel=3)
#colour_sensor4 = Colour_sensor.ColourSensor(channel=4)
#ultrasonic = ULTRASONIC_CODE.ObstacleDetector(trigger_pin=23, echo_pin=24)
camera= Detection.AI()

def camera_listener():
    camera= Detection.AI()

    return


def sensor_listener():
    """
    Continuously monitors the color sensors to detect bin alignment.
    Updates the global variable `bin_aligned` based on sensor readings.
    """
    global bin_aligned , bin_location, program_running, next_road
    while program_running:
        rgbL = colour_sensor1.read() # Left sensor
        rgbR = colour_sensor2.read() # Right sensor
        green_valueL = rgbL['green']
        green_valueR = rgbR['green']
        next_road = camera.detect_road()
        if green_valueL >= GREEN_THRESHOLD:
            bin_aligned = True
            bin_location = "left"
        elif green_valueR >= GREEN_THRESHOLD:
            bin_aligned = True
            bin_location = "right"
        else:
            bin_aligned = False
            bin_location = None
        time.sleep(0.5)  # Polling interval

def input_listener():
    """
    Runs in a separate thread to listen for mode change or exit requests.
    """
    global current_mode, switch_requested, program_running
    while program_running:
        user_input = input("\n(Type 'switch (idle, start, stop, return)").strip().lower()
        if user_input.startswith("switch"):
            parts = user_input.split()
            if len(parts) == 2:
                current_mode = parts[1]
                switch_requested = True
            else:
                print("Usage: switch <mode>")
        elif user_input == "exit":
            program_running = False
            switch_requested = True  # To break current mode loop


def idle_mode():
    print("[IDLE MODE] Running... (type 'switch <mode>')")
    while not switch_requested and program_running:
        time.sleep(1)  # Simulate background idle behavior

def start_mode():
    print('starting...')
    global bin_aligned
    while not switch_requested and program_running:
        if next_road != None:
            print("Next road detected:", next_road)
        if bin_aligned == False:
            motor_assembly.forward()
        elif bin_aligned == True:
             motor_assembly.stop()
             if bin_location == "left":
                print("Picking up bin on the left")
                #servo pickup code for left bin
             elif bin_location == "right":
                print("Picking up bin on the right")
                #servo pickup code for left bin

def return_mode():
    print("returning...")
    while not switch_requested and program_running:
        motor_assembly.backward()
        time.sleep(1)
        motor_assembly.stop()


def stop_mode():
    print("stopping...")
    while not switch_requested and program_running:
        motor_assembly.stop()


def main():
    # Function dictionary
    modes = {
        "idle": idle_mode,
        "start": start_mode,
        "stop": stop_mode,
        "return": return_mode
    }

    # Start the input listener in a separate thread
    listener_thread = threading.Thread(target=input_listener, daemon=True)
    listener_thread.start()
    sensor_listener_thread = threading.Thread(target=sensor_listener, daemon=True)
    sensor_listener_thread.start()


    global switch_requested

    while program_running:
        mode_function = modes.get(current_mode, idle_mode)
        switch_requested = False
        mode_function()  # Run the selected mode
        print(f">>> Switching mode to '{current_mode}'...\n")


    print("Program exited.")

if __name__ == "__main__":
    main()
