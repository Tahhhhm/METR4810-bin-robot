from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
import smbus2 as smbus

MUX_ADDR = 0x70
bus = smbus.SMBus(1)
channel = 1

bus.write_byte(MUX_ADDR, 1<<channel)
# Initialize the servo controller
controller = PiicoDev_Servo_Driver()

# Create servo object on channel 4
arm = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)
grabber = PiicoDev_Servo(controller, 2)
axial = PiicoDev_Servo(controller, 3, midpoint_us=1500, range_us=1800)

print("Starting autonomous servo motion...")

#def dispose():
# arm.speed = -0.3
# sleep_ms(1200)
# arm.speed = 0
# sleep_ms(1000) 

axial.speed = 0.8
sleep_ms(1000)
axial.speed = 0
sleep_ms(1500)
axial.speed = -0.8
sleep_ms(1000)
axial.speed = 0
sleep_ms(3000)