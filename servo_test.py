from gpiozero import AngularServo, Device
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Create a factory for pigpio (just for the servo)
servo_factory = PiGPIOFactory()

# Use pigpio factory only for this servo
servo_arm = AngularServo(18, min_angle=-90, max_angle=90, pin_factory=servo_factory)

# Move the servo
servo_arm.angle = -90
sleep(3)
servo_arm.angle = 0
sleep(3)
servo_arm.angle = 90
sleep(3)
