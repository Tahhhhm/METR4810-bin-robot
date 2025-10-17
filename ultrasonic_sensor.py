import time
import RPi.GPIO as GPIO

# Define pins
TRIG = 17  # GPIO17
ECHO = 27  # GPIO27

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Ensure trigger is low
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    # Send 10us pulse to trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start

    # Distance in cm
    distance = pulse_duration * 17150  # Speed of sound = 34300 cm/s
    distance = round(distance, 2)

    return distance

try:
    while True:
        dist = get_distance()
        print("Distance:", dist, "cm")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
