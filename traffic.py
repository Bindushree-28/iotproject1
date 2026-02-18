import RPi.GPIO as GPIO
import time
import requests

# GPIO setup
GPIO.setmode(GPIO.BCM)

RED = 17
YELLOW = 27
GREEN = 22

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

# ThingSpeak API
API_KEY = "YOUR_API_KEY"
URL = "https://api.thingspeak.com/update"

def send_data(light):
    data = {"api_key": API_KEY, "field1": light}
    requests.post(URL, data=data)

try:
    while True:
        # Green
        GPIO.output(GREEN, True)
        GPIO.output(YELLOW, False)
        GPIO.output(RED, False)
        send_data("GREEN")
        time.sleep(5)

        # Yellow
        GPIO.output(GREEN, False)
        GPIO.output(YELLOW, True)
        GPIO.output(RED, False)
        send_data("YELLOW")
        time.sleep(2)

        # Red
        GPIO.output(GREEN, False)
        GPIO.output(YELLOW, False)
        GPIO.output(RED, True)
        send_data("RED")
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
