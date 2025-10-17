from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=27, trigger=17)

try:
    while True:
        distance = sensor.distance * 100
        print("Distance: ", sensor.distance, "cm")
        sleep(1)
except KeyboardInterrupt:
    print("Stopped")
