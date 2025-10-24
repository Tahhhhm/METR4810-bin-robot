from Colour_sensor import ColourSensor
#from Test import dispose
from PiicoDev_Unified import sleep_ms

# Create the colour sensor instance
sensor1 = ColourSensor(channel=0)
sensor2 = ColourSensor(channel=1)
sensor3 = ColourSensor(channel=2)
sensor4 = ColourSensor(channel=3)

# Threshold for green detection
GREEN_THRESHOLD = 400 

print("System running — waiting for green detection...")

while True:
    print(sensor1.readRGB)
    print(sensor2.readRGB)
    print(sensor3.readRGB)
    print(sensor4.readRGB)
    sleep_ms(1000)
    
    #            # returns a dict like {'red': 123, 'green': 456, 'blue': 789}
    # green_value = rgb['green']
    # print(f"Green: {green_value}")

    # if green_value >= GREEN_THRESHOLD:
    #     print("Green detected! Activating disposal sequence...")
    #     #dispose()
    #     sleep_ms(2000)
    # else:
    #     print("No green detected.")

    # sleep_ms(10)  # adjust frequency of checks