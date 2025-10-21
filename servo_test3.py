
from gpiozero import AngularServo 
from time import sleep 

servo_arm = AngularServo(18, min_angle= 0, max_angle= 180, min_pulse_width=0.0005, max_pulse_width=0.0025)

# Sweep the servo slowly 0->90°
for x in range(0,90,5):
    servo_arm.angle = x
    sleep(2)
