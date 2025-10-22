from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms
import smbus2 as smbus
MUX_ADDR = 0x70
bus = smbus.SMBus(1)    

class ColourSensor:
    def __init__(self, channel):
        bus.write_byte(MUX_ADDR, 1<<channel)
        self.colourSensor = PiicoDev_VEML6040()
        self.channel = channel

    def readRGB(self):
        bus.write_byte(MUX_ADDR, 1<<self.channel)
        data = self.colourSensor.readRGB() # Read the sensor (Colour space: Red Green Blue)
        return data

