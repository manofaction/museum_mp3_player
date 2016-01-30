#!usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

while True:
    if (GPIO.input(23)==False):
        os.system('mpg123 -q mp3_files/track_1_test.mp3')

    if (GPIO.input(24)==False):
        os.system('mpg123 -q mp3_files/track_2_test.mp3')

    sleep(1);
