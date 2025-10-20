import Colour_sensor 
colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
import time

while True:
    data1 = colour_sensor1.readRGB(channel=0)
    data2 = colour_sensor2.readRGB(channel=1)
    data3 = colour_sensor3.readRGB(channel=2)
    data4 = colour_sensor4.readRGB(channel=3)
    print(data1)
    print(data2)
    print(data3)
    print(data4)
    time.sleep(2)