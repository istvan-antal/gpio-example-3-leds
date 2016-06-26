#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

GPIO.output(11, GPIO.HIGH)

try:
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()