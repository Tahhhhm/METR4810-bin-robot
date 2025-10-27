from Colour_sensor import ColourSensor   # adjust filename to match your .py file name
from PiicoDev_Unified import sleep_ms

#left front 1
#right front 3
#right bin 4

left_front_sensor = ColourSensor(channel=1)  # create sensor instance
right_front_sensor = ColourSensor(channel=3)
right_bin_sensor = ColourSensor(channel=4)

while True:
    rgb1 = left_front_sensor.readRGB()    
    rgb2 = right_front_sensor.readRGB()
    rgb3 = right_bin_sensor.readRGB()     # returns a dict like {'red': 123, 'green': 456, 'blue': 789}
       # extract the green component
   
    print('left front', rgb1)
    print('right front',rgb2)
    print('right bin', rgb3)

    sleep_ms(1000)
