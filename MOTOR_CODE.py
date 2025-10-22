import RPi.GPIO as GPIO
from time import sleep
import random


class Motor:
    def __init__(self, in1, in2, in3, in4, EnA, EnB):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.EnA = EnA
        self.EnB = EnB

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Setup GPIO pins
        pins = [in1, in2, in3, in4, EnA, EnB]
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def forward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.EnA, GPIO.HIGH)

        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        GPIO.output(self.EnB, GPIO.HIGH)

    def backward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.EnA, GPIO.HIGH)

        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        GPIO.output(self.EnB, GPIO.HIGH)

    def turn_left(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.EnA, GPIO.HIGH)

        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        GPIO.output(self.EnB, GPIO.HIGH)

    def turn_right(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.EnA, GPIO.HIGH)

        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        GPIO.output(self.EnB, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.EnA, GPIO.LOW)

        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        GPIO.output(self.EnB, GPIO.LOW)

    def turn(self, degree):
        # Turns the robot by a specified degree
        # Positive = Clockwise (right), Negative = Counter-clockwise (left)
        turn_time = abs(degree) / 90.0 * 0.5  # Adjust 0.5 as per calibration

        if degree > 0:
            self.turn_right()
        elif degree < 0:
            self.turn_left()
        else:
            return

        sleep(turn_time)
        self.stop()

    def straight(self):
        self.forward()
        sleep(5.5)
        self.stop()

    def hairpin(self, direction):
        self.forward()
        sleep(2)
        self.stop()
        if direction == "right":
            self.turn(-90)
        else:
            self.turn(90)
        self.forward()
        sleep(1)
        self.stop()

    def curve(self, direction):
        self.forward()
        sleep(2)
        self.stop()
        if direction == "left":
            self.turn(75)
        else:
            self.turn(-75)
        self.forward()
        sleep(0.5)
        self.stop()

    def crossroad(self, direction):
        self.forward()
        sleep(2)
        if direction == "forward":
            self.forward()
            sleep(1)
        elif direction == "left":
            self.turn(45)
            self.forward()
            sleep(1.5)
        elif direction == "right":
            self.turn(-45)
            self.forward()
            sleep(1.5)
        else:
            self.forward()
            sleep(5)
        self.stop()

    def delivery_point(self):
        self.forward()
        sleep(1.5)
        self.stop()

    def process_tiles(self, next_tile, tile_list):
        tile_list.append(next_tile)
        tile = tile_list[0]

        if tile in ["straight", "Chicane"]:
            self.straight()

        elif tile in ["Right_turn", "right_hairpin"]:
            self.turn_right()
            sleep(1)
            self.stop()

        elif tile in ["left_curve", "left_hairpin"]:
            self.turn_left()
            sleep(1)
            self.stop()

        elif tile == "crossroad":
            direction = random.choice(["forward", "right", "left"])
            self.crossroad(direction)

        tile_list.pop(0)
