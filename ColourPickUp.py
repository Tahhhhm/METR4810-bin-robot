from Colour_sensor import ColourSensor
#from Test import dispose
from PiicoDev_Unified import sleep_ms

# Create the colour sensor instance
FrontL = ColourSensor(channel=1)
#BinL = ColourSensor(channel=2)
BinR = ColourSensor(channel=4)
FrontR = ColourSensor(channel=3)
#sensor3 = ColourSensor(channel=2)
#sensor4 = ColourSensor(channel=3)

# Threshold for green detection
GREEN_THRESHOLD = 400
ROAD_THRESHOLD = 240 
REDBIN_THRESHOLD = 250
YELLOWBIN_THRESHOLD = 500
print("System running — waiting for green detection...")

while True:
    #print(FrontL.readRGB())
    #print(FrontR.readRGB())
    #print(BinL.readRGB())
    print(BinR.readRGB())
    sleep_ms(1000)
    
    # returns a dict like {'red': 123, 'green': 456, 'blue': 789}

    #off_road_left = FrontL.readRGB()['green'] > GREEN_THRESHOLD 
    #off_road_right = FrontR.readRGB()['green'] > GREEN_THRESHOLD
    bin_right_red = BinR.readRGB()['blue']>REDBIN_THRESHOLD
    if bin_right_red:
        print("Picking Bin")
    #if off_road_right and off_road_left:
    #     print("stopping...")
    # elif off_road_right:
    #     print("need to turn left")
    # elif off_road_left:
    #     print("need to turn right")
    # else:
    #     print("onward")
    sleep_ms(1000)  # adjust frequency of checks