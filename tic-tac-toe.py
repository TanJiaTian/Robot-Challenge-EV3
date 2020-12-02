#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# Grabbing blocks
# Defining motors and sensors
motor_right = ev3.LargeMotor('outD')
motor_left = ev3.LargeMotor('outA')
motor_medium =ev3.MediumMotor('outC')
ts = ev3.TouchSensor()
cl = ev3.ColorSensor()

while not ts.value():
    sleep(0.01)

def

def grab_the_blocks():
    for x in range(0,100):
        cl.mode = 'COL-REFLECT'
        x = cl.value()
        if x == 12:

