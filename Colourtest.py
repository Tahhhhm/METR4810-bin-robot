from Colour_sensor import ColourSensor   # adjust filename to match your .py file name
from PiicoDev_Unified import sleep_ms

sensor = ColourSensor(channel=0)  # create sensor instance

while True:
    rgb = sensor.readRGB()             # returns a dict like {'red': 123, 'green': 456, 'blue': 789}
    green_value = rgb['green']         # extract the green component
    print(f"Green value: {green_value}")
    sleep_ms(500)
