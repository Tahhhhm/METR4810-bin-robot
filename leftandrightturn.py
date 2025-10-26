import MOTOR_CODE
from time import sleep

def main():
    # Initialize motor (replace pins with your actual wiring)
    motor = MOTOR_CODE.Motor(in1=20, in2=16, in3=26, in4=19, EnA=21, EnB=13)
    
    print("[TEST] Starting motor test...")
    
    # Set motor speed to 30%
    motor.set_speed(30)

    try:
        # Test turning left
        print("[TEST] Turning LEFT...")
        motor.turn_left()
        sleep(2)  # turn for 2 seconds
        motor.stop()
        sleep(1)

        # Test turning right
        print("[TEST] Turning RIGHT...")
        motor.turn_right()
        sleep(2)
        motor.stop()
        sleep(1)

        # Done
        print("[TEST] Test complete.")

    except KeyboardInterrupt:
        print("[TEST] Interrupted by user.")

    finally:
        motor.stop()
        motor.cleanup()
        print("[TEST] Motors stopped and GPIO cleaned up.")

if __name__ == "__main__":
    main()
