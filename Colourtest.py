from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms
import smbus2 as smbus

# Address for the TCA9548A I2C multiplexer
MUX_ADDR = 0x70
bus = smbus.SMBus(1)

class ColourSensor:
    def __init__(self, channel):
        bus.write_byte(MUX_ADDR, 1 << channel)
        # Use longest integration time for more stable readings
        self.colourSensor = PiicoDev_VEML6040(integration_time=320)
        self.channel = channel

    def readRGB(self, samples=5):
        """Read RGB values, average multiple samples, and normalize to 0-255"""
        total = {'red': 0, 'green': 0, 'blue': 0}

        for _ in range(samples):
            bus.write_byte(MUX_ADDR, 1 << self.channel)
            data = self.colourSensor.readRGB()
            for k in total:
                total[k] += data[k]
            sleep_ms(50)  # short delay between samples

        # Average the readings
        averaged = {k: total[k] / samples for k in total}

        # Normalize to 0-255 based on max value
        max_val = max(averaged.values()) or 1  # prevent division by zero
        normalized = {k: int(255 * v / max_val) for k, v in averaged.items()}

        print(f"{normalized['blue']} Blue  {normalized['green']} Green  {normalized['red']} Red")
        return normalized

    def readGreen(self, samples=5):
        """Return only the normalized green value"""
        data = self.readRGB(samples)
        return data['green']

# ---------------------------
# Create a ColourSensor object
# ---------------------------
sensor = ColourSensor(channel=0)   # 0 = SD0/SC0, 1 = SD1/SC1, etc.

print("Reading normalized color values from VEML6040 on channel 0...")

# ---------------------------
# Read green value continuously
# ---------------------------
while True:
    green_value = sensor.readGreen(samples=5)
    print(f"Normalized Green: {green_value}")
    sleep_ms(1000)  # wait 1 second between readings
