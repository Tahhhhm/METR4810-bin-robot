from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from gpiozero import Button
import smbus2 as smbus
MUX_ADDR = 0x70
bus = smbus.SMBus(1)    
from signal import pause
from time import sleep

bus.write_byte(MUX_ADDR, 1<<2)
controller = PiicoDev_Servo_Driver()

servo_claw = PiicoDev_Servo(controller, 2, degrees=180)
servo_arm = PiicoDev_Servo(controller, 3, midpoint_us=1500, range_us=1800)
servo_base = PiicoDev_Servo(controller, 4, midpoint_us=1400, range_us=1800)

micro_1 = Button(23, pull_up=True) # Lower
micro_0 = Button(22, pull_up=True) # Upper

def on_press_rest():
    #micro_0.when_pressed = None
    print("Lower Limit Switch hit...")
    #servo_claw.angle = 0
    #servo_arm.speed = 0
    #sleep_ms(500)
    #servo_arm.speed = -0.1

    
def on_press_dump():
    #micro_1.when_pressed = None  # Disable to prevent reentry
    print("Upper Limit Switch hit")

    #servo_arm.speed = 0
    #sleep_ms(500)

def on_release():
    print("Switch Released")

def grab():
    servo_claw.angle = 90
    sleep(1)

def release():
    servo_claw.angle = 0
    sleep(1)

micro_0.when_pressed = on_press_rest
micro_0.when_released = on_release
micro_1.when_pressed = on_press_dump
micro_1.when_released = on_release

try:
    #servo_base.speed = -0.2
    #sleep_ms(1300)
    #servo_base.speed = 0
    #sleep(0.5)
    #servo_arm.speed = 0.1
    #pause()
    servo_claw.angle = 0
    sleep(3)
    servo_claw.angle = 90
    sleep(2)
    servo_arm.speed = -0.1
    sleep(2.5)
    servo_arm.speed = 0
except KeyboardInterrupt:
    print("Shutting down safely...")
    servo_arm.speed = 0
    servo_base.angle = 90
    servo_claw.angle = 90

