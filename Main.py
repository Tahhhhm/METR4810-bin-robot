import Colour_sensor 
colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
import time

while True:
    colour_sensor1.readRGB()
    colour_sensor2.readRGB()
    colour_sensor3.readRGB()
    colour_sensor4.readRGB()
    time.sleep(2)