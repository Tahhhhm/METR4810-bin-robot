from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from gpiozero import Button
from signal import pause

#initialise servo driver 
controller = PiicoDev_Servo_Driver()
micro_0 = Button(26, pull_up=True)
micro_1 = Button(16, pull_up=True)

def on_press_rest():
    # Just stops
    print("Lower Limit Switch hit...")
    servo4.speed = 0
    
def on_press_dump():
    # Stops then reverses
    print("Upper Limit Switch hit")
    servo4.speed = 0
    sleep_ms(500)
    servo4.speed = -0.3

def on_release():
    print("Switch Released")

micro_0.when_pressed = on_press_rest
micro_0.when_released = on_release
micro_1.when_pressed = on_press_dump
micro_1.when_released = on_release


# servo1 = PiicoDev_Servo(controller, 1, degrees=180)
#servo2 = PiicoDev_Servo(controller, 2, degrees=180)
# servo3 = PiicoDev_Servo(controller, 3, degrees=180)
servo4 = PiicoDev_Servo(controller, 4, midpoint_us=1500, range_us = 1800)

servo4.speed = 0.1
print("DUMP")                                                       

# Hit limit switch
# servo4.speed = -0.5 
# print("RETURN")


# Hit limit switch
pause()
