from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# Initialize the servo controller
controller = PiicoDev_Servo_Driver()

# Create servo object on channel 4
arm = PiicoDev_Servo(controller, 1, midpoint_us=1500, range_us=1800)
grabber = PiicoDev_Servo(controller, 2)
axial = PiicoDev_Servo(controller, 3, midpoint_us=1500, range_us=1800)

print("Starting autonomous servo motion...")

for angle in range(1, 181, 5):  # Step of 5 degrees
        grabber.angle = angle
        print(f"Angle: {angle}°")
        sleep_ms(100)  # Delay between movements (adjust as needed)

    # Sweep back from 180° to 1°
for angle in range(180, 0, -5):
        grabber.angle = angle
        print(f"Angle: {angle}°")
        sleep_ms(100)

print("Sweep complete.")

""" arm.speed = -0.3
sleep_ms(1200)
arm.speed = 0
sleep_ms(1000) """