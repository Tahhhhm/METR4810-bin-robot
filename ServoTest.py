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
servo_arm = PiicoDev_Servo(controller, 4, midpoint_us=1500, range_us=1800)
servo_base = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)

micro_1 = Button(18, pull_up=True)
micro_0 = Button(23, pull_up=True)

servo_arm.speed = 0.5
sleep_ms(500)
servo_arm.speed = 0
