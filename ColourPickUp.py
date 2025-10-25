from Colour_sensor import ColourSensor
#from Test import dispose
from PiicoDev_Unified import sleep_ms

# Create the colour sensor instance
FrontL = ColourSensor(channel=1)
FrontR = ColourSensor(channel=3)
#sensor3 = ColourSensor(channel=2)
#sensor4 = ColourSensor(channel=3)

# Threshold for green detection
GREEN_THRESHOLD = 400
ROAD_THRESHOLD = 240 

print("System running — waiting for green detection...")

while True:
    print(FrontL.readRGB())
    print(FrontR.readRGB())
    sleep_ms(1000)
    
    #            # returns a dict like {'red': 123, 'green': 456, 'blue': 789}

    off_road_left = FrontL.readRGB()['green'] > GREEN_THRESHOLD 
    off_road_right = FrontL.readRGB()['green'] > GREEN_THRESHOLD
    if off_road_right:
        print("need to turn left")
    elif off_road_left:
        print("need to turn right")
    elif off_road_right and off_road_left:
        print("stopping...")
    else:
        print("onward")

    sleep_ms(1000)  # adjust frequency of checks