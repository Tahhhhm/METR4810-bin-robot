import Colour_sensor 
import ULTRASONIC_CODE
import MOTOR_CODE
import threading
import time

current_mode = "idle"
switch_requested = False
program_running = True
motor_assembly = MOTOR_CODE.Motor(17, 27, 22, 23, 24, 18)
colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
ultrasonic = ULTRASONIC_CODE.ObstacleDetector(trigger_pin=23, echo_pin=24)

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
    while not switch_requested and program_running:
        motor_assembly.forward()
        #code everything for detection etc

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

    global switch_requested

    while program_running:
        mode_function = modes.get(current_mode, idle_mode)
        switch_requested = False
        mode_function()  # Run the selected mode
        print(f">>> Switching mode to '{current_mode}'...\n")

    print("Program exited.")

if __name__ == "__main__":
    main()
