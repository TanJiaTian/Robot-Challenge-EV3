#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# making a loop square (task 1)
# Defining motors and sensor(s)
motor_left = ev3.LargeMotor('outA')
motor_right = ev3.LargeMotor('outD')
ts = ev3.TouchSensor()

while not ts.value():
    sleep(0.01)

def go_straight_short():
# move motor on both sides for 512 degress of rotation with 500deg/sec
    motor_left.run_to_rel_pos(position_sp=512, speed_sp=500, stop_action = 'brake')
    motor_right.run_to_rel_pos(position_sp=512, speed_sp=500, stop_action = 'brake')
# wait till the motor has stopped
    motor_right.wait_while('running')
    motor_left.wait_while('running')

def go_straight_long():
# move motor on both sides for 1024 degress of rotation with 500deg/sec
    motor_left.run_to_rel_pos(position_sp=1024, speed_sp=500, stop_action = 'brake')
    motor_right.run_to_rel_pos(position_sp=1024, speed_sp=500, stop_action = 'brake')
# wait till the motor has stopped
    motor_right.wait_while('running')
    motor_left.wait_while('running')

def turn_left():
    # move motor left for 90 deg rotation
    motor_right.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
    motor_left.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')

def turn_right():
    # move motor right for 90 deg rotation
    motor_right.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
    motor_left.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')

def turn180():
    # move motor right for 180 deg rotation
    motor_right.run_timed(time_sp=2009.859422, speed_sp=-300, stop_action='hold')
    motor_left.run_timed(time_sp=2009.859422, speed_sp=300, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')




go_straight_short()

turn_left()

go_straight_short()

turn_right()

go_straight_long()

turn_right()

go_straight_long()

turn_right()

go_straight_long()

turn_right()

go_straight_short()

turn_left()

go_straight_short()

turn180()
