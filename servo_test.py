
from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle = -90, max_angle=90) #arm 
servo.angle = 0 # mid-point 
sleep(2)

servo.angle = 90
sleep(2)
