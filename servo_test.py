from gpiozero import AngularServo
from time import sleep

servo_arm = AngularServo(18, min_angle=-90, max_angle=90)

while True:
    servo_arm.angle = -90
    sleep(2)
    servo_arm.angle = 0
    sleep(2)
    servo_arm.angle = 90
    sleep(2)




