#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# Detecting colors
motor_right = ev3.LargeMotor('outD')
motor_left = ev3.LargeMotor('outA')
# connect color sensor
cl = ev3.ColorSensor()
ts = ev3.TouchSensor()

while not ts.value():
    sleep(0.01)

def move_straight():
    # move motor on both sides for 250ms with 500deg/sec
    motor_left.run_timed(time_sp=250, speed_sp=500, stop_action = "brake")
    motor_right.run_timed(time_sp=250, speed_sp=500, stop_action = "brake")
    # wait till the motor has stopped
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    # stop for 3 seconds
    sleep(3)    

def color():
    # define color mode
    cl.mode = 'COL-COLOR'
    if cl.value() == 0:
        ev3.Sound.speak("No color")
        sleep(3)
    if cl.value() == 1:
        ev3.Sound.speak("Black")
        sleep(3)
    if cl.value() == 2:
        ev3.Sound.speak("Blue")
        sleep(3)
    if cl.value() == 4:
        ev3.Sound.speak("Yellow")
        sleep(3)
    if cl.value() == 5:
        ev3.Sound.speak("Red")
        sleep(3)
  
  move_straight()
  color()
