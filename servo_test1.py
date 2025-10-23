from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from PiicoDev_Unified import sleep_ms
from gpiozero import Button


# controller = PiicoDev_Servo_Driver()
# servo4 = PiicoDev_Servo(controller, 4, midpoint_us=1500, range_us = 1800)

# servo4.speed = 0.5
# sleep_ms(1000) 
# servo4.speed = 0


micro_0 = Button(4, pull_up=True)
micro_0.wait_for_press()
print("The button was pressed!")
