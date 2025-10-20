
from gpiozero import AngularServo
from time import sleep

min_angle = -180
max_angle = 180

servo_arm = AngularServo(18, min_angle=min_angle, max_angle=max_angle)

while True:
    for i in range(-90, 90, 10):
        servo_arm.angle = i
        print(f"Servo angle set to: {i} degrees")
        sleep(0.5)
    i =-90
    




