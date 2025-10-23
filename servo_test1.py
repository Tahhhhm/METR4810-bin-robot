from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from PiicoDev_Unified import sleep_ms

controller = PiicoDev_Servo_Driver()
servo4 = PiicoDev_Servo(controller, 4, midpoint_us=1500, range_us = 1800)

servo4.speed = -0.1
sleep_ms(3000) 
servo4.speed = 0