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

# Limit switches
# micro_lower = Button(23, pull_up=True)  # Lower switch (was upper)
# micro_upper = Button(22, pull_up=True)  # Upper switch (was lower)


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


# --- Limit switch callbacks ---
# def on_press_lower():
#     """Now acts as the previous 'Upper Limit Switch hit'."""
#     print("Lower Limit Switch (was upper) hit.")
#     servo_arm.speed = 0
#     sleep(1)
#     release()  # Drop the bin


# def on_press_upper():
#     """Now acts as the previous 'Lower Limit Switch hit'."""
#     print("Upper Limit Switch (was lower) hit.")
#     servo_arm.speed = 0
#     sleep(1)

#     grab()  # Hold the bin
#     servo_arm.speed = 0.3  # Raise bin
#     sleep(1)

#     # Rotate base 90 degrees
#     servo_base.speed = -0.2
#     sleep_ms(1200)
#     servo_base.speed = 0
#     print("Base rotation complete.")


# def on_release():
#     """Triggered when either switch is released."""
#     print("Switch released.")


# --- Attach event handlers (swapped) ---
# micro_lower.when_pressed = on_press_lower
# micro_lower.when_released = on_release
# micro_upper.when_pressed = on_press_upper
# micro_upper.when_released = on_release


# --- Main loop / startup sequence ---
try:
    print("System initialized. Starting motion sequence...")
    release()
    sleep(1)
    servo_arm.speed = 0.2
    sleep_ms(900)
    servo_arm.speed = 0
    sleep(1)
    grab()
    servo_arm.speed = -0.3
    sleep_ms(900)
    servo_arm.speed = 0
    sleep(1)
    servo_base.speed = 0.8
    sleep_ms(450)
    servo_base.speed = 0
    sleep(1)
    servo_arm.speed = 0.3
    sleep_ms(100)
    servo_arm.speed = 0

except KeyboardInterrupt:
    print("\nShutting down safely...")
    servo_arm.speed = 0
    servo_base.angle = 90
    servo_claw.angle = 90
    print("Servos stopped. Exiting.")