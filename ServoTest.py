from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from gpiozero import Button
import smbus2 as smbus
from time import sleep

# I2C multiplexer setup
MUX_ADDR = 0x70
bus = smbus.SMBus(1)
bus.write_byte(MUX_ADDR, 1 << 2)  # Select channel 2 on the multiplexer

# Servo driver
controller = PiicoDev_Servo_Driver()

# Continuous rotation servo on channel 4
servo_arm = PiicoDev_Servo(controller, 4)

# Optional limit switches
micro_0 = Button(26, pull_up=True)
micro_1 = Button(22, pull_up=True)

while True:
    # Rotate slowly forward (clockwise)
    servo_arm.angle(100)  # 100 ≈ slight forward motion
    print("→ Forward (slow)")
    sleep(2)

    # Stop
    servo_arm.angle(90)  # 90 = stop for continuous servos
    print("■ Stop")
    sleep(1)

    # Rotate slowly backward (counterclockwise)
    servo_arm.angle(80)  # 80 ≈ slight reverse motion
    print("← Reverse (slow)")
    sleep(2)

    # Stop
    servo_arm.angle(90)
    print("■ Stop")
    sleep(1)
