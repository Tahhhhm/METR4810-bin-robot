# MOTOR CODE

# This code is responsible for the motion subsystem of the METR4810
# Team 1 Garbage Truck
# Requirements:
#   sudo apt update
#   sudo apt install python3-gpiozero

from gpiozero import Motor
from time import sleep

# Initialize motors (adjust GPIO pins accordingly)
motor_left = Motor(forward=23, backward=24)
motor_right = Motor(forward=17, backward=27)

def fwd():
    print("ONWARD")
    motor_left.forward()
    motor_right.forward()
    #sleep(duration)

def bwd():
    print("RETREAT")
    motor_left.backward()
    motor_right.backward()
    #sleep(duration)

def turn(degree):
    """
    Turns the robot by a specified degree.
    Positive = Clockwise (right turn)
    Negative = Counter-clockwise (left turn)
    """
    # Simple estimation: 90 degrees ≈ 0.5 seconds (need to calibrate this)
    turn_time = (abs(degree) / 90.0) * 1  # adjust 0.5 based on real-world testing

    if degree > 0:
        # Clockwise: left forward, right backward
        print("RIGHT")
        motor_left.forward()
        motor_right.backward() # REPLACE VALUE ON TESTING
    elif degree < 0:
        print("LEFT")
        # Anticlockwise: left backward, right forward
        motor_left.backward()
        motor_right.forward()  # REPLACE VALUE ON TESTING
    else:
        return  # No turning

    sleep(turn_time)

def stop():
    motor_left.stop()
    motor_right.stop()

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


turn(degree=-90)
stop()
motor_left.close()
motor_right.close()
