from Colour_sensor import ColourSensor   # adjust filename to match your .py file name
from PiicoDev_Unified import sleep_ms

sensor1 = ColourSensor(channel=0)  # create sensor instance
sensor2 = ColourSensor(channel=1)
sensor3 = ColourSensor(channel=2)
sensor4 = ColourSensor(channel=3)
while True:
    rgb1 = sensor1.readRGB()    
    rgb2 = sensor2.readRGB()
    rgb3 = sensor3.readRGB()
    rgb4 = sensor4.readRGB()         # returns a dict like {'red': 123, 'green': 456, 'blue': 789}
       # extract the green component
   
    print(rgb1)
    print(rgb2)
    print(rgb3)
    print(rgb4)
    sleep_ms(1000)
