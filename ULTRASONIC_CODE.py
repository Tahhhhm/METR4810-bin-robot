from gpiozero import DistanceSensor
from time import sleep

class ObstacleDetector:
    def __init__(self, trigger_pin, echo_pin):
        self.sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin)

    def obstacles_present(self):
            distance = self.sensor.distance * 100  # convert to cm
            return distance
