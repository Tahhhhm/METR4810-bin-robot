from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms
import smbus2 as smbus
MUX_ADDR = 0x70
bus = smbus.SMBus(1)

class ColourSensor:
    def __init__(self, channel):
        bus.write_byte(MUX_ADDR, 1<<channel)
        self.colourSensor = PiicoDev_VEML6040()

    def readRGB(self,channel):
        bus.write_byte(MUX_ADDR, 1<<channel)
        data = self.colourSensor.readRGB() # Read the sensor (Colour space: Red Green Blue)
        red = data['red'] # extract the RGB information from data
        grn = data['green']
        blu = data['blue']
        print(str(blu) + " Blue  " + str(grn) + " Green  " + str(red) + " Red")
        return data

