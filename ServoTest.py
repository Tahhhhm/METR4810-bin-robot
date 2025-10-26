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

servo_claw = PiicoDev_Servo(controller, 3, degrees=180)
servo_arm = PiicoDev_Servo(controller, 4, midpoint_us=1500, range_us=1800)
servo_base = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)

micro_0 = Button(26, pull_up=True)
micro_1 = Button(22, pull_up=True)  

while True:
    # Slow forward
    servo_arm.pulse_width_us(1550)
    print("→ Forward (slow)")
    sleep(2)

    # Stop
    servo_arm.pulse_width_us(1500)
    print("■ Stop")
    sleep(1)

    # Slow reverse
    servo_arm.pulse_width_us(1450)
    print("← Reverse (slow)")
    sleep(2)

    # Stop
    servo_arm.pulse_width_us(1500)
    print("■ Stop")
    sleep(1)