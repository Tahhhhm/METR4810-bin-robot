from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# Initialize the servo controller
controller = PiicoDev_Servo_Driver()

# Create servo object on channel 4
arm = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)
grabber = PiicoDev_Servo(controller, 2)
axial = PiicoDev_Servo(controller, 3, midpoint_us=1500, range_us=1800)

print("Starting autonomous servo motion...")

# Move forward slowly
print("Moving forward...")
arm.speed = -0.5
sleep_ms(1000)
print("stop")
arm.speed = 0
sleep_ms(10000)