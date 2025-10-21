import RPi.GPIO as GPIO
from time import sleep
import random



# Initialize motors (adjust GPIO pins accordingly)

class Motor:
    def __init__(self, in1, in2, in3, in4, EnA, EnB):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.EnA = EnA
        self.EnB = EnB
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(in2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(in3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(in3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(in4, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(EnA, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(EnB, GPIO.OUT, initial=GPIO.LOW)
 
    def forward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.EnA, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        GPIO.output(self.EnB, GPIO.HIGH)
        tile_list.pop(0)
        

    def backward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.EnA, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        GPIO.output(self.EnB, GPIO.HIGH)
        tile_list.pop(0)

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
        
    def processTiles(self, tile_list, side):
        tile=tile_list[0]
        if tile == "straight" or "Chicane" :
            self.forward(tile_list)
        elif tile == "Right_turn" or "right_hairpin":
            self.turn_right(tile_list)
        elif tile == "left_curve" or "left_hairpin":
            self.turn_left(tile_list)
        elif tile == "crossroad":
            choice = random.choice(["forward", "right", "left"])
            
            if choice == "forward":
                self.forward(tile_list)
            elif choice == "right":
                self.turn_right(tile_list)
            elif choice == "left":
                self.turn_left(tile_list)

 
            
    
    """
    def turn(degree, speed=1.0):
        
        Turns the robot by a specified degree.
        Positive = Clockwise (right turn)
        Negative = Counter-clockwise (left turn)
        
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
"""