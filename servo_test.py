from gpiozero import AngularServo
from time import sleep

servo_arm = AngularServo(18, min_angle=-90, max_angle=90)

servo_arm.angle = -90
sleep(3)
servo_arm.angle = 0
sleep(3)
servo_arm.angle = 90
sleep(3)




