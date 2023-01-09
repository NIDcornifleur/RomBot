import RPi.GPIO as GPIO
import time

channel = 5

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def light_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def light_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


if __name__ == '__main__':
    try:
        light_on(channel)
        time.sleep(.5)
        light_off(channel)
        time.sleep(999999999999999)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()

