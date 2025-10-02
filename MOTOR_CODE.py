# MOTOR CODE

# This code is responsible for the motion subsystem of the METR4810
# Team 1 Garbage Truck
# Requirements:
#   sudo apt update
#   sudo apt install python3-gpiozero

from gpiozero import Motor
from time import sleep

# Initialize motors (adjust GPIO pins accordingly)
motor_left = Motor(forward=17, backward=18)
motor_right = Motor(forward=22, backward=23)

def fwd(speed=1.0, duration=1.0):
    motor_left.forward(speed)
    motor_right.forward(speed)
    #sleep(duration)
    stop()

def bwd(speed=1.0, duration=1.0):
    motor_left.backward(speed)
    motor_right.backward(speed)
    #sleep(duration)
    stop()

def turn(degree, speed=1.0):
    """
    Turns the robot by a specified degree.
    Positive = Clockwise (right turn)
    Negative = Counter-clockwise (left turn)
    """
    # Simple estimation: 90 degrees ≈ 0.5 seconds (need to calibrate this)
    turn_time = abs(degree) / 90.0 * 0.5  # adjust 0.5 based on real-world testing

    if degree > 0:
        # Clockwise: left forward, right backward
        motor_left.forward(speed)
        motor_right.backward(speed) # REPLACE VALUE ON TESTING
    elif degree < 0:
        # Anticlockwise: left backward, right forward
        motor_left.backward(speed)
        motor_right.forward(speed)  # REPLACE VALUE ON TESTING
    else:
        return  # No turning

    sleep(turn_time)
    stop()


def stop():
    motor_left.stop()
    motor_right.stop()

from time import sleep

# --- Motion Macros (based on your Arduino logic) ---

def straight():
    fwd()
    sleep(5.5)

def hairpin(dir):
    if dir == "right":
        fwd()
        sleep(2)
        stop()
        turn(-90)
        fwd()
        sleep(1)
    else:
        fwd()
        sleep(2)
        stop()
        turn(90)
        fwd()
        sleep(1)

def curve(dir):
    if dir == "left":
        fwd()
        sleep(2)
        stop()
        turn(75)
        fwd()
        sleep(0.5)
    else:
        fwd()
        sleep(2)
        stop()
        turn(-75)
        fwd()
        # Duration for final movement after turn not specified, assuming 0.5
        sleep(0.5)

def crossroad(dir):
    fwd()
    sleep(2)
    if dir == "fwd":
        fwd()
        sleep(1)
    elif dir == "left":
        turn(45)
        fwd()
        sleep(1.5)
    elif dir == "right":
        turn(-45)
        fwd()
        sleep(1.5)
    else:
        fwd()
        sleep(5)

def delivery_point():
    fwd()
    sleep(1.5)

# Main loop simulation
if __name__ == '__main__':
    fwd(speed=0.8)
    bwd(speed=0.8)
    turn(degree=90, speed=0.8)
    turn(degree=-90, speed=0.8)

    stop()
