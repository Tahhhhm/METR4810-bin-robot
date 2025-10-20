import Colour_sensor 
import ULTRASONIC_CODE
import MOTOR_CODE
#colour_sensor1 = Colour_sensor.ColourSensor(channel=0)
#colour_sensor2 = Colour_sensor.ColourSensor(channel=1)
#colour_sensor3 = Colour_sensor.ColourSensor(channel=2)
#colour_sensor4 = Colour_sensor.ColourSensor(channel=3)
u_sensor = ULTRASONIC_CODE.ObstacleDetector(trigger_pin=23, echo_pin=24)
import time
motor_assembly = Motor(23, 24, 17, 27, 18, 2) # This is what we're using on the prototype
motor_assembly.forward()

#while True:
    #colour_sensor1.readRGB()
    #colour_sensor2.readRGB()
    #colour_sensor3.readRGB()
    #colour_sensor4.readRGB()
    #time.sleep(2)
    #u_sensor.obstacles_present()
    #time.sleep(2)
