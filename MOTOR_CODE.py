import RPi.GPIO as GPIO
from time import sleep
import random

# Global flag (set externally in main control file)
tile_action_paused = False  


class Motor:
    def __init__(self, in1, in2, in3, in4, EnA=None, EnB=None):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.EnA = EnA
        self.EnB = EnB

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Setup all motor pins as outputs
        for pin in [in1, in2, in3, in4]:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        # Optional: if EnA/EnB provided, set them HIGH (always enabled)
        if EnA is not None:
            GPIO.setup(EnA, GPIO.OUT)
            GPIO.output(EnA, GPIO.HIGH)
            self.PWMA = GPIO.PWM(EnA, 100)
            self.PWMA.start(0)
        
            
        if EnB is not None:
            GPIO.setup(EnB, GPIO.OUT)
            GPIO.output(EnB, GPIO.HIGH)
            self.PWMB = GPIO.PWM(EnB, 100)
            self.PWMB.start(0)

        self.speed = 50
        print("[MOTOR] Initialized GPIO pins.")
        
    #Set speed 
    def set_speed(self, speed):
        """Set motor speed as a percentage (0–100)."""
        self.speed = max(0, min(100, speed))
        self.pwmA.ChangeDutyCycle(self.speed)
        self.pwmB.ChangeDutyCycle(self.speed)
    # ========== BASIC MOVEMENTS ==========
    
    def forward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        #print("[MOTOR] Moving forward")

    def backward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        #print("[MOTOR] Moving backward")

    def turn_left(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        #print("[MOTOR] Turning left")

    def turn_right(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        #print("[MOTOR] Turning right")

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        #print("[MOTOR] Stopped")

    def cleanup(self):
        self.stop()
        GPIO.cleanup()
        #print("[MOTOR] GPIO cleaned up")

    # ========== TURN BY ANGLE (approximate) ==========
    def turn(self, degree):
        """
        Turn the robot by an approximate degree.
        Positive = Clockwise (right)
        Negative = Counter-clockwise (left)
        """
        turn_time = abs(degree) / 90.0 * 0.5  # ~0.5s per 90°, calibrate this
        if degree > 0:
            #print(f"[MOTOR] Turning right {degree}°")
            self.turn_right()
        elif degree < 0:
            #print(f"[MOTOR] Turning left {degree}°")
            self.turn_left()
        else:
            return
        sleep(turn_time)
        self.stop()

    # ========== TILE SEQUENCE EXECUTION ==========
    def processTiles(self, tile_list):
        """
        Executes a pre-defined motor sequence for each tile type.
        Will pause automatically if tile_action_paused is True.
        """
        global tile_action_paused

        for tile in tile_list:
            #print(f"[PROCESS TILE] Executing tile: {tile}")

            # Wait if paused
            while tile_action_paused:
                self.stop()
                sleep(0.1)

            # --- Straight path ---
            if tile == "straight":
                self.forward()
                sleep(5.5)

            # --- Right turn tile ---
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

            # --- Left turn tile ---
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

            # --- Crossroad tile (random path for testing) ---
            elif tile == "crossroad":
                choice = random.choice(["forward", "right", "left"])
                # print(f"[CROSSROAD] Randomly chosen direction: {choice}")

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

            # After every tile motion
            self.stop()
            sleep(0.5)

        # print("[PROCESS TILE] Tile sequence complete.")