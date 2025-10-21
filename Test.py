from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

# Initialize the servo controller
controller = PiicoDev_Servo_Driver()

# Create servo object on channel 4
servo4 = PiicoDev_Servo(controller, 4, midpoint_us=1500, range_us=1800)

print("Starting autonomous servo motion...")

try:
    # Move forward slowly
    print("Moving forward...")
    servo4.speed = 0.3
    sleep_ms(1000)
    print("stop")
    servo4.speed = 0
    sleep_ms(10000)

except KeyboardInterrupt:
    # Stop the servo safely if user ends the program
    print("\nProgram interrupted. Stopping servo...")
    servo4.speed = 0
