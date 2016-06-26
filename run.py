#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

try:
    while 1:
        GPIO.output(13, GPIO.LOW)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(100)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(100)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(100)
except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()