from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from gpiozero import Button
import smbus2 as smbus
from time import sleep

# --- Hardware setup ---
MUX_ADDR = 0x70
bus = smbus.SMBus(1)
bus.write_byte(MUX_ADDR, 1 << 2)

controller = PiicoDev_Servo_Driver()

servo_claw = PiicoDev_Servo(controller, 2, degrees=180)
servo_arm = PiicoDev_Servo(controller, 3, midpoint_us=1500, range_us=1800)
servo_base = PiicoDev_Servo(controller, 4, midpoint_us=1400, range_us=1800)

# --- Servo movement functions ---
def grab():
    """Close the claw to grab the bin."""
    print("Grabbing...")
    servo_claw.angle = 90
    sleep(1)


def release():
    """Open the claw to release the bin."""
    print("Releasing...")
    servo_claw.angle = 0
    sleep(1)

# --- Main loop / startup sequence ---
def pickup_bin():
    try:
        print("DUMP")
        release()
        sleep(1)
        servo_arm.speed = 0.2
        sleep_ms(800)
        servo_arm.speed = 0
        sleep(1)
        grab()

        servo_arm.speed = -0.5
        sleep_ms(600)
        servo_arm.speed = 0
        sleep(1)
        servo_base.speed = 0.8
        sleep_ms(450)
        servo_base.speed = 0
        sleep(1)
        servo_arm.speed = -0.3
        sleep_ms(900)
        servo_arm.speed = 0

        print("PUT BACK")
        sleep(1)
        servo_base.speed = -0.8
        sleep_ms(450)
        servo_base.speed = 0
        sleep(1)
        servo_arm.speed = 0.2
        sleep_ms(1100)
        servo_arm.speed = 0
        sleep(1)
        release()
        sleep(1)

    except KeyboardInterrupt:
        print("\nShutting down safely...")
        servo_arm.speed = 0
        servo_base.angle = 90
        servo_claw.angle = 90
        print("Servos stopped. Exiting.")