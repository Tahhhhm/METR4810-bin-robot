import RPi.GPIO as GPIO
from time import sleep
import random

tile_action_paused = False  

class Motor:
    def __init__(self, in1, in2, in3, in4, EnA=None, EnB=None):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.EnA = EnA
        self.EnB = EnB
        self.pwmA = None
        self.pwmB = None

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Setup motor control pins
        for pin in [in1, in2, in3, in4]:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        # Setup enable pins with PWM
        if EnA is not None:
            GPIO.setup(EnA, GPIO.OUT)
            self.pwmA = GPIO.PWM(EnA, 1000)  # 1kHz frequency
            self.pwmA.start(25)              # 25% duty cycle = quarter speed

        if EnB is not None:
            GPIO.setup(EnB, GPIO.OUT)
            self.pwmB = GPIO.PWM(EnB, 1000)
            self.pwmB.start(25)

        print("[MOTOR] Initialized GPIO pins and PWM (25% speed).")

    # ========== BASIC MOVEMENTS ==========
    def forward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def backward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def turn_left(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def turn_right(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

    def set_speed(self, duty):
        """Change motor speed (0–100%)."""
        if self.pwmA:
            self.pwmA.ChangeDutyCycle(duty)
        if self.pwmB:
            self.pwmB.ChangeDutyCycle(duty)
        print(f"[MOTOR] Speed set to {duty}%")

    def cleanup(self):
        self.stop()
        if self.pwmA:
            self.pwmA.stop()
        if self.pwmB:
            self.pwmB.stop()
        GPIO.cleanup()
        print("[MOTOR] GPIO cleaned up")

    # ========== TURN BY ANGLE (approximate) ==========
    def turn(self, degree):
        turn_time = abs(degree) / 90.0 * 0.5
        if degree > 0:
            self.turn_right()
        elif degree < 0:
            self.turn_left()
        else:
            return
        sleep(turn_time)
        self.stop()

    # ========== TILE SEQUENCE EXECUTION ==========
    def processTiles(self, tile_list):
        global tile_action_paused

        for tile in tile_list:
            while tile_action_paused:
                self.stop()
                sleep(0.1)

            if tile == "straight":
                self.forward()
                sleep(5.5)
            elif tile == "Right_turn":
                self.forward()
                sleep(2)
                self.turn_right()
                sleep(1)
                self.forward()
                sleep(1)
                self.turn_right()
                sleep(1)
                self.forward()
                sleep(1)
            elif tile == "left_turn":
                self.forward()
                sleep(2)
                self.turn_left()
                sleep(1)
                self.forward()
                sleep(1)
                self.turn_left()
                sleep(1)
                self.forward()
                sleep(1)
            elif tile == "crossroad":
                choice = random.choice(["forward", "right", "left"])
                if choice == "forward":
                    self.forward()
                    sleep(5.5)
                elif choice == "right":
                    self.forward()
                    sleep(2.8)
                    self.turn_right()
                    sleep(2)
                    self.forward()
                    sleep(1.5)
                elif choice == "left":
                    self.forward()
                    sleep(2.8)
                    self.turn_left()
                    sleep(2)
                    self.forward()
                    sleep(1.5)

            self.stop()
            sleep(0.5)
