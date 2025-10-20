import Colour_sensor 
colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
import time

while True:
    data1 = colour_sensor1.readRGB()
    data2 = colour_sensor2.readRGB()
    data3 = colour_sensor3.readRGB()
    data4 = colour_sensor4.readRGB()
    print(data1)
    print(data2)
    print(data3)
    print(data4)
    time.sleep(2)