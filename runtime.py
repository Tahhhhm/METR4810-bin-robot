# This code combines all the functions and models and lays out operational procedure of the METR4810
# Miniturized Garbage Bin Prototype
from MOTOR_CODE import Motor
from SERVO_CODE import ServoController
from ULTRASONIC_CODE import ObstacleDetector
from Detection import AI
from time import sleep
from gpiozero import AngularServo
import time
import Colour_sensor 
import RPi.GPIO as GPIO


motor_assembly = Motor(23, 24, 17, 27, 2, 3) # This is what we're using on the prototype
servo_assembly = ServoController(0, 1 ,2)
detector = ObstacleDetector(trigger_pin=17, echo_pin=27)
colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
models = AI()
outside_bounds = False
on_green = False
move_list = []

#Keeps robot on track and avoid obstacles
def boundary_check():
    return on_green

def obstacle_check():
    if detector.obstacles_present():
        print("Obstacle detected!")

        # While inside bounds, keep turning to avoid obstacle
        while not outside_bounds:
            motor_assembly.turn(1)  # Turn right
            time.sleep(0.5)         # Let the turn happen

            if boundary_check():
                print("On boundary (e.g., green area), reversing direction.")
                # Turn the other way until obstacle is cleared
                while detector.obstacles_present():
                    motor_assembly.turn(-1)  # Turn left
                    time.sleep(0.5)
                print("Obstacle cleared while turning away from boundary.")
                break  # Exit once obstacle is no longer present

            # Re-check obstacle
            if not detector.obstacles_present():
                print("Obstacle cleared.")
                break

    else:
        print("No obstacle.")
        
def queueTiles(road_tile_list):
    next_tile = road_tile_list[:-1]
    if next_tile == "left curve":

    
    

# Navigate (near entire) track to find delivery zones and bins
if __name__ == "runtime":
    bin_list = models.detect_bin()
    road_tile_list = models.detect_road()
    queueTiles(road_tile_list)
    
    

# Use A* search algorithm to compute the shortest path to each bin

# Travel to the closest bin and record the lid colour

# Extract contents from the bin

# Move to the deposit zone

# If bin lid was red, deposit to landfill pile, else deposit to recycling pile

# Repeat until all bins are cleared — collection is complete
