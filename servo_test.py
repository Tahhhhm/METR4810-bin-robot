
from gpiozero import AngularServo
from time import sleep

min_angle = -90
max_angle = 90
servo_arm = AngularServo(18, min_angle=min_angle, max_angle=max_angle)

servo_arm.angle = 90




