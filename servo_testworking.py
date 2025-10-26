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
servo_base = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)

micro_1 = Button(18, pull_up=True)
micro_0 = Button(24, pull_up=True)

def on_press_rest():
    # Just stops
    print("Lower Limit Switch hit...")
    servo_arm.speed = 0
    
def on_press_dump():
    # Stops then reverses
    print("Upper Limit Switch hit")

    servo_arm.speed = 0
    sleep_ms(500)
    servo_arm.speed = 0.1
    #turn90()
    #release()

def on_release():
    print("Switch Released")

def grab():
    servo_claw.angle = 90
    sleep(2)

def release():
    servo_claw.angle = 0
    sleep(2)

def turn180():
    print("Turning 180 degrees")
    servo_base.speed = 0.1
    sleep(7)
    servo_base.speed = 0

def turnAnti180():
    print("Turning 180 degrees anti")
    servo_base.speed = -0.1
    sleep(7)
    servo_base.speed = 0

def turn90():
    print("Turning 90 degrees")
    servo_base.speed = 0.1
    sleep(3.5)
    servo_base.speed = 0

def turnAnti90():
    print("Turning 90 degrees anti")
    servo_base.speed = -0.1
    sleep(3.5)
    servo_base.speed = 0

micro_0.when_pressed = on_press_rest
micro_0.when_released = on_release
micro_1.when_pressed = on_press_dump
micro_1.when_released = on_release

try:
    servo_arm.speed = 1
    sleep_ms(1000)
    servo_arm.speed = 0.2
    sleep_ms(1000)
    servo_arm.speed = -0.5    
except KeyboardInterrupt:
    print("Shutting down safely...")
    servo_arm.speed = 0
    servo_base.speed = 0
    servo_claw.angle = 0

