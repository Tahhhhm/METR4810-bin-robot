from gpiozero import Servo
from time import sleep

# === Servo Setup ===
# Adjust "min_pulse_width" and "max_pulse_width" depending on your servo type
grab = Servo(8, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
arm = Servo(9, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
axial = Servo(10, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

# gpiozero Servo values range from -1 (full clockwise), 0 (stop), +1 (full anti-clockwise)
# so we’ll map Arduino’s 0–180 into -1…+1

def write(servo, angle):
    # map 0–180 (Arduino style) to -1…+1 (gpiozero style)
    servo.value = (angle - 90) / 90.0

# === Setup ===
# this is just to reset grabber to close position
write(grab, 160)  

while True:
    sleep(3)
    # slow speed of arm bending right then back to default position (upright)

    # .write(val) value is 0–89 (clockwise). 0 is full speed, 89 is lowest
    write(arm, 65)
    # delay(val) it took around 900ms for arm to bend down 90 degrees at speed 65
    # (note*: this was when the arm is not holding anything yet, you may need to twiddle
    # with the timing a little to account for different weights)
    sleep(0.9)

    write(arm, 90)
    # 90 means stop movement. Arm stops moving for 1500ms between each movement
    sleep(1.5)

    # .write(val) value is 91–180 (anti-clockwise). 180 is full speed, 91 is lowest
    write(arm, 135)
    sleep(0.9)

    write(arm, 90)
    sleep(3)

    # grabber open position at 160 degrees
    write(grab, 160)
    sleep(1.5)
    # grabber closes position at 120 degrees after 1500ms
    write(grab, 120)
    sleep(1.5)

    # note*: I haven't tried the axial turn with the arm attached so timing value will be very different,
    # nevertheless the code is about the same logic as arm, just from a different axis

    write(axial, 65)
    # arm faces to the right
    sleep(0.7)

    write(axial, 90)
    sleep(1.5)

    write(axial, 135)
    # arm faces to the left
    sleep(0.7)

    break  # in Arduino you had while(true);, in Python we just break to stop program