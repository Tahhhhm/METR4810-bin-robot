from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from PiicoDev_Unified import sleep_ms


controller = PiicoDev_Servo_Driver()

servo_bottom = PiicoDev_Servo(controller, 1, midpoint_us = 1400, range_us = 1800)
servo_arm= PiicoDev_Servo(controller, 2, midpoint_us = 1500, range_us = 1800) # arm  z 
servo_claw = PiicoDev_Servo(controller, 3)

def pickup_left():
    print("Starting pickup procedure")
    servo_arm.speed = -0.1 # go down i.e move left 
    sleep_ms(1500)
    servo_arm.speed = 0 
    
    #grab bin 
    servo_claw.angle = 90
    sleep_ms(1000)

    # lift arm 
    servo_arm.speed = 0.1 #move up 
    sleep_ms(500)
    servo_arm.speed = 0 


def pickup_right(): 
    #lower arm 
    servo_arm.speed = -0.1 
    sleep_ms(500)
    servo_arm.speed = 0

    #grab bin 
    servo_claw.angle = 90 
    sleep_ms(1000)

    #lift arm 
    servo_arm.speed = 0.1
    sleep_ms(1500)
    servo_arm.speed = 0 


def release(bin_colour): 
    if bin_colour == 'red': 
        servo_bottom.speed = 0.1 #rotate bottom servo cw 
        sleep_ms(900)
        servo_bottom.speed = 0 
        servo_arm.speed = 0.1 #tilt arm backwards 
        sleep_ms(900)
        servo_arm.speed = 0 

        #return red bin to original position 
        servo_bottom.speed = 0.1 #rotate 90 deg 
        sleep_ms(900) 
        servo_bottom.speed = 0 
        servo_arm.speed = 0.1 #lower arm 
        sleep_ms(900) 
        servo_arm.speed = 0
        servo_claw.angle = 0 #open claw 
    
    else: 
        servo_bottom.speed = -0.1 #rotate cw or ccw ? (test)
        sleep_ms(900)
        servo_bottom.speed = 0 
        servo_arm.speed = 0.1 #tilt arm backwards 
        sleep_ms(900)
        servo_arm.speed = 0 
        
        #return yellow bin to original position 
        servo_bottom.speed = 0.1 #rotate 90 deg 
        sleep_ms(900)
        servo_bottom.speed = 0 
        servo_arm.speed = 0.1 #lower arm 
        sleep_ms(500)
        servo_arm.angle = 0 
        servo_claw.angle = 0 #open claw 


        #return arm to centre position 
        servo_arm.speed = 0.1 
        sleep_ms(500)
        servo_arm.speed = 0 
        servo_bottom = 0.1 #rotate base 90 deg 
        sleep_ms(500)
        servo_bottom.speed = 0 







## 45RPM -> ms timings
## 90 degrees (1/4 rotation) --> 333.3
## 180 degrees (1/4 rotation) --> 667.2
## 270 degrees (1/4 rotation) --> 1000
## 360 degrees (1/4 rotation) --> 1333.3

