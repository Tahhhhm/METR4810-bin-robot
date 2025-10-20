
from gpiozero import AngularServo
from time import sleep

min_angle = -89
max_angle = 89

servo_arm = AngularServo(18, min_angle=-89, max_angle=89)

while True:
    for i in range(-89, 89, 1):
        servo_arm.angle = i
        print(f"Servo angle set to: {i} degrees")
        sleep(1)
    




