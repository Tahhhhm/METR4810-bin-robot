from gpiozero import AngularServo
from time import sleep



servo_arm = AngularServo(18, min_angle= 0, max_angle= 180)

servo_arm.angle = 0
sleep(2) #time to reach the position 
