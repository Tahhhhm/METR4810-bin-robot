from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms
import smbus2 as smbus

# Address for the TCA9548A I2C multiplexer
MUX_ADDR = 0x70
bus = smbus.SMBus(1)

class ColourSensor:
    def __init__(self, channel):
        bus.write_byte(MUX_ADDR, 1 << channel)
        self.colourSensor = PiicoDev_VEML6040()
        self.channel = channel

    def readRGB(self):
        bus.write_byte(MUX_ADDR, 1 << self.channel)
        data = self.colourSensor.readRGB()  # Read the sensor (Colour space: Red Green Blue)
        red = data['red']    # extract the RGB information from data
        grn = data['green']
        blu = data['blue']
        print(str(blu) + " Blue  " + str(grn) + " Green  " + str(red) + " Red")
        return data

# ---------------------------
# Create a ColourSensor object
# ---------------------------

# Change the number here depending on which TCA9548A channel your VEML6040 is connected to:
sensor = ColourSensor(channel=0)   # 0 = SD0/SC0, 1 = SD1/SC1, etc.

print("Reading colour values from VEML6040 on channel 0...")

# ---------------------------
# Read RGB values continuously
# ---------------------------
while True:
    sensor.readRGB()
    sleep_ms(1000)  # wait 1 second between readings
