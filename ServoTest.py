from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from gpiozero import Button
import smbus2 as smbus
from time import sleep

# Select MUX channel 2 for the servo driver
MUX_ADDR = 0x70
bus = smbus.SMBus(1)
bus.write_byte(MUX_ADDR, 1 << 2)

# Initialize servo driver and servos
controller = PiicoDev_Servo_Driver()

servo_claw = PiicoDev_Servo(controller, 2, degrees=180)
servo_arm = PiicoDev_Servo(controller, 4, midpoint_us=1500, range_us=1800)
servo_base = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)

# Micro switches
micro_1 = Button(18, pull_up=True)
micro_0 = Button(23, pull_up=True)

print("Arm starting... moving forward")

# Start moving forward
servo_arm.speed = 0.5

while True:
    # If the first microswitch is pressed
    if micro_1.is_pressed:
        print("Micro_1 pressed → stopping for 2s then reversing")
        servo_arm.speed = 0      # Stop
        sleep(2)                 # Pause
        servo_arm.speed = -0.5   # Reverse direction
        print("Now moving backward")

        # Wait until micro_0 is pressed
        while not micro_0.is_pressed:
            sleep(0.05)

        print("Micro_0 pressed → reversing a little, then stopping")
        servo_arm.speed = 0.5    # Move slightly forward again
        sleep(0.5)
        servo_arm.speed = 0      # Stop
        print("Arm stopped completely")
        break  # Exit loop safely (optional — remove if you want it to repeat)

    sleep(0.05)  # Small loop delay to reduce CPU load
