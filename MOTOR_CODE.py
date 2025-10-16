"""
MOTOR CODE

This code defines a MotorController class responsible for the motion subsystem
of the METR4810 Team 1 Garbage Truck.

"""

from gpiozero import Motor
from time import sleep

class MotorController:
    """
    Controls the movement of a two-motor robot using GPIO pins.
    
    Args:
        pin_list (list): A list of four GPIO pins in the following order:
                         [left_forward, left_backward, right_forward, right_backward]
    """

    def __init__(self, pin_list):
        if len(pin_list) != 4:
            raise ValueError("pin_list must contain exactly four GPIO pin numbers.")
        lf, lb, rf, rb = pin_list
        self.motor_left = Motor(forward=lf, backward=lb)
        self.motor_right = Motor(forward=rf, backward=rb)

    def fwd(self):
        """Moves the robot forward."""
        print("ONWARD")
        self.motor_left.forward()
        self.motor_right.forward()

    def bwd(self):
        """Moves the robot backward."""
        print("RETREAT")
        self.motor_left.backward()
        self.motor_right.backward()

    def turn(self, degree):
        """
        Turns the robot by a specified degree.

        Args:
            degree (int or float): Degrees to turn.
                                   Positive for clockwise (right),
                                   Negative for counter-clockwise (left).
        """
        turn_time = (abs(degree) / 90.0) * 1  # Adjust this based on actual behavior
        if degree > 0:
            print("RIGHT")
            self.motor_left.forward()
            self.motor_right.backward()
        elif degree < 0:
            print("LEFT")
            self.motor_left.backward()
            self.motor_right.forward()
        else:
            return  # No turning

        sleep(turn_time)

    def stop(self):
        """Stops both motors."""
        self.motor_left.stop()
        self.motor_right.stop()

    # --- Motion Macros (based on motor_simple.ino logic) ---

    def straight(self):
        """Drives straight for a predefined time."""
        self.fwd()
        sleep(5.5)

    def hairpin(self, direction):
        """
        Performs a hairpin turn.

        Args:
            direction (str): "left" or "right"
        """
        self.fwd()
        sleep(2)
        self.stop()
        if direction == "right":
            self.turn(-90)
        else:
            self.turn(90)
        self.fwd()
        sleep(1)

    def curve(self, direction):
        """
        Performs a curved turn.

        Args:
            direction (str): "left" or "right"
        """
        self.fwd()
        sleep(2)
        self.stop()
        if direction == "left":
            self.turn(75)
        else:
            self.turn(-75)
        self.fwd()
        sleep(0.5)

    def crossroad(self, direction):
        """
        Navigates a crossroad.

        Args:
            direction (str): "fwd", "left", "right", or any other string for default.
        """
        self.fwd()
        sleep(2)
        if direction == "fwd":
            self.fwd()
            sleep(1)
        elif direction == "left":
            self.turn(45)
            self.fwd()
            sleep(1.5)
        elif direction == "right":
            self.turn(-45)
            self.fwd()
            sleep(1.5)
        else:
            self.fwd()
            sleep(5)

    def delivery_point(self):
        """Drives forward to simulate arriving at a delivery point."""
        self.fwd()
        sleep(1.5)

    def close(self):
        """Closes motor resources (optional in many setups, but good practice)."""
        self.motor_left.close()
        self.motor_right.close()


# --- Example usage (uncomment for testing on actual hardware) ---
# controller = MotorController([23, 24, 17, 27])
# controller.turn(degree=-90)
# controller.stop()
# controller.close()
