import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define pins
LED = 18
BUTTON = 23

# Setup pins
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

try:
    while True:
        state = GPIO.input(BUTTON)  # read button

        if state == 1:   # button pressed
            GPIO.output(LED, True)   # LED ON
        else:
            GPIO.output(LED, False)  # LED OFF

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
