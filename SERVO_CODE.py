from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver
from PiicoDev_Unified import sleep_ms

class ServoController:
    """
    A class to control a robotic arm that picks up and releases bins using servo motors.

    Attributes:
        servo_bottom (PiicoDev_Servo): Controls the base rotation.
        servo_arm (PiicoDev_Servo): Controls the vertical arm movement.
        servo_claw (PiicoDev_Servo): Controls the claw (gripper) opening and closing.
    """

    def __init__(self, servo_buses):
        """
        Initialize the BinPickupRobot with servo bus numbers.

        Args:
            servo_buses (list or tuple): A list or tuple of 3 integers representing the
                bus numbers for the bottom, arm, and claw servos, respectively.
        """
        if len(servo_buses) != 3:
            raise ValueError("servo_buses must be a list or tuple of exactly 3 integers.")

        bottom_bus, arm_bus, claw_bus = servo_buses

        self.controller = PiicoDev_Servo_Driver()

        self.servo_bottom = PiicoDev_Servo(self.controller, bottom_bus, midpoint_us=1400, range_us=1800)
        self.servo_arm = PiicoDev_Servo(self.controller, arm_bus, midpoint_us=1500, range_us=1800)
        self.servo_claw = PiicoDev_Servo(self.controller, claw_bus)

    def pickup_left(self):
        """
        Executes the pickup routine on the left side:
        - Lowers the arm
        - Closes the claw to grab a bin
        - Lifts the arm
        """
        print("Starting pickup procedure (left)")
        self.servo_arm.speed = -0.1  # lower arm
        sleep_ms(1500)
        self.servo_arm.speed = 0

        self.servo_claw.angle = 90  # close claw
        sleep_ms(1000)

        self.servo_arm.speed = 0.1  # lift arm
        sleep_ms(500)
        self.servo_arm.speed = 0

    def pickup_right(self):
        """
        Executes the pickup routine on the right side:
        - Lowers the arm
        - Closes the claw to grab a bin
        - Lifts the arm
        """
        print("Starting pickup procedure (right)")
        self.servo_bottom.speed = 0.1
        sleep_ms(900)

    def release(self, bin_colour):
        """
        Releases a bin based on its color by rotating and tilting the arm,
        then opening the claw and returning to the default position.

        Args:
            bin_colour (str): The color of the bin to release. 
                Must be either 'red' or another supported color (e.g., 'yellow').
        """
        print(f"Releasing bin: {bin_colour}")
        if bin_colour == 'red':
            # Rotate and tilt for red bin
            self.servo_bottom.speed = 0.1
            sleep_ms(900)
            self.servo_bottom.speed = 0

            self.servo_arm.speed = 0.1
            sleep_ms(900)
            self.servo_arm.speed = 0

            # Return to original position
            self.servo_bottom.speed = 0.1
            sleep_ms(900)
            self.servo_bottom.speed = 0

            self.servo_arm.speed = 0.1
            sleep_ms(900)
            self.servo_arm.speed = 0

            self.servo_claw.angle = 0  # open claw

        else:
            # Rotate and tilt for other bin (e.g. yellow)
            self.servo_bottom.speed = -0.1
            sleep_ms(900)
            self.servo_bottom.speed = 0

            self.servo_arm.speed = 0.1
            sleep_ms(900)
            self.servo_arm.speed = 0

            # Return to original position
            self.servo_bottom.speed = 0.1
            sleep_ms(900)
            self.servo_bottom.speed = 0

            self.servo_arm.speed = 0.1
            sleep_ms(500)
            self.servo_arm.speed = 0

            self.servo_claw.angle = 0  # open claw

            # Reset arm and base
            self.servo_arm.speed = 0.1
            sleep_ms(500)
            self.servo_arm.speed = 0

            self.servo_bottom.speed = 0.1
            sleep_ms(500)
            self.servo_bottom.speed = 0
