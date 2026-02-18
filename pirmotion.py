import RPi.GPIO as GPIO
import time

# GPIO mode
GPIO.setmode(GPIO.BCM)

# Pin setup
PIR = 17
LED = 18

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

print("Waiting for motion...")

try:
    while True:
        motion = GPIO.input(PIR)

        if motion == 1:
            print("Motion Detected!")
            GPIO.output(LED, True)   # LED ON
            time.sleep(2)            # LED stays ON
        else:
            GPIO.output(LED, False)  # LED OFF

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
