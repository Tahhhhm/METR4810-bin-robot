from PiicoDev_Unified import sleep_ms
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from gpiozero import Button
import smbus2 as smbus
from time import sleep


class BinPickupSystem:
    def __init__(self):
        # --- Hardware setup ---
        self.MUX_ADDR = 0x70
        self.bus = smbus.SMBus(1)
        self.bus.write_byte(self.MUX_ADDR, 1 << 2)

        self.controller = PiicoDev_Servo_Driver()

        # Servos
        self.servo_claw = PiicoDev_Servo(self.controller, 2, degrees=180)
        self.servo_arm = PiicoDev_Servo(self.controller, 3, midpoint_us=1500, range_us=1800)
        self.servo_base = PiicoDev_Servo(self.controller, 4, midpoint_us=1400, range_us=1800)

        print("BinPickupSystem initialized.")

    # --- Servo movement helpers ---
    def grab(self):
        """Close the claw to grab the bin."""
        print("Grabbing...")
        self.servo_claw.angle = 90
        sleep(1)

    def release(self):
        """Open the claw to release the bin."""
        print("Releasing...")
        self.servo_claw.angle = 0
        sleep(1)

    # --- Main sequence ---
    def pickup_bin(self):
        """Perform full pickup and dump sequence."""
        try:
            print("DUMP SEQUENCE START")

            # Initial release (open claw)
            self.release()
            sleep(1)

            # Lower arm
            self.servo_arm.speed = 0.2
            sleep_ms(800)
            self.servo_arm.speed = 0
            sleep(1)

            # Grab bin
            self.grab()

            # Raise arm
            self.servo_arm.speed = -0.5
            sleep_ms(600)
            self.servo_arm.speed = 0
            sleep(1)

            # Rotate base (dump)
            self.servo_base.speed = 0.8
            sleep_ms(450)
            self.servo_base.speed = 0
            sleep(1)

            # Lower arm to dump
            self.servo_arm.speed = -0.3
            sleep_ms(900)
            self.servo_arm.speed = 0

            print("PUT BACK SEQUENCE")
            sleep(1)

            # Rotate base back
            self.servo_base.speed = -0.8
            sleep_ms(450)
            self.servo_base.speed = 0
            sleep(1)

            # Raise arm back up
            self.servo_arm.speed = 0.2
            sleep_ms(1100)
            self.servo_arm.speed = 0
            sleep(1)

            # Release bin
            self.release()
            sleep(1)

            print("Sequence complete.")

        except KeyboardInterrupt:
            self.shutdown()

    def shutdown(self):
        """Safely stop all servos."""
        print("\nShutting down safely...")
        self.servo_arm.speed = 0
        self.servo_base.angle = 90
        self.servo_claw.angle = 90
        print("Servos stopped. Exiting.")


# --- Run example ---
if __name__ == "__main__":
    robot = BinPickupSystem()
    robot.pickup_bin()
