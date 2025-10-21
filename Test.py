from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from PiicoDev_Unified import sleep_ms

controller = PiicoDev_Servo_Driver()
servo = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)

print("Testing servo angles...")

for angle in [0, 90, 180, 90, 0]:
    print("Angle:", angle)
    servo.angle = angle
    sleep_ms(1000)
