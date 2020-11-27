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

def grab_the_blocks():
    for x in range(0,8):
        cl.mode = 'COL-COLOR'
        x = cl.value()
        if x == 1:
            # move motor on both sides for 1100ms with 500deg/sec
            motor_left.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # move motor right for 90 deg rotation
            motor_right.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
            motor_left.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # move motor on both sides for 1100ms with 500deg/sec
            motor_left.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # move motor right for 90 deg rotation
            motor_right.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
            motor_left.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # move motor on both sides for 1100ms with 500deg/sec
            motor_left.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # grab action
            motor_medium.run_timed(time_sp=3500, speed_sp=-1000, stop_action="brake")
            motor_medium.wait_while('running')
            # move motor left for 180 deg rotation
            motor_right.run_timed(time_sp=2009.859422, speed_sp=300, stop_action='hold')
            motor_left.run_timed(time_sp=2009.859422, speed_sp=-300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # move motor on both sides for 2200ms with 500deg/sec
            motor_left.run_timed(time_sp=2200, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=2200, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # move motor right for 90 deg rotation
            motor_right.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
            motor_left.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # move motor on both sides for 1100ms with 500deg/sec
            motor_left.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # move motor left for 90 deg rotation
            motor_right.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
            motor_left.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # release action
            motor_medium.run_timed(time_sp=3500, speed_sp=500, stop_action="brake")
            motor_medium.wait_while('running')
            # sleep 2 seconds for new colour detection
            sleep(2)


        if x == 2:
            # move motor on both sides for 2200ms with 500deg/sec
            motor_left.run_timed(time_sp=2200, speed_sp=500, stop_action="hold")
            motor_right.run_timed(time_sp=2200, speed_sp=500, stop_action="hold")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # grab action
            motor_medium.run_timed(time_sp=3500, speed_sp=-1000, stop_action="brake")
            motor_medium.wait_while('running')
            # move motor on both sides for 2200ms with -500deg/sec
            motor_left.run_timed(time_sp=2200, speed_sp=-500, stop_action="hold")
            motor_right.run_timed(time_sp=2200, speed_sp=-500, stop_action="hold")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # release action
            motor_medium.run_timed(time_sp=3500, speed_sp=500, stop_action="brake")
            motor_medium.wait_while('running')
            # sleep 2 seconds for new colour detection
            sleep(2)


        if x == 4:
            # move motor on both sides for 1100ms with 500deg/sec
            motor_left.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # move motor right for 90 deg rotation
            motor_right.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
            motor_left.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # move motor on both sides for 1100ms with 500deg/sec
            motor_left.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # move motor left for 90 deg rotation
            motor_right.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
            motor_left.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # move motor on both sides for 1100ms with 500deg/sec
            motor_left.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # grab action
            motor_medium.run_timed(time_sp=3500, speed_sp=-1000, stop_action="brake")
            motor_medium.wait_while('running')
            # move motor right for 180 deg rotation
            motor_right.run_timed(time_sp=2009.859422, speed_sp=-300, stop_action='hold')
            motor_left.run_timed(time_sp=2009.859422, speed_sp=300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # move motor on both sides for 2200ms with 500deg/sec
            motor_left.run_timed(time_sp=2200, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=2200, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # move motor right for 90 deg rotation
            motor_right.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
            motor_left.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # move motor on both sides for 1100ms with 500deg/sec
            motor_left.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            motor_right.run_timed(time_sp=1100, speed_sp=500, stop_action="brake")
            # wait till the motor has stopped
            motor_right.wait_while('running')
            motor_left.wait_while('running')
            # move motor right for 90 deg rotation
            motor_right.run_timed(time_sp=1046.801782, speed_sp=-300, stop_action='hold')
            motor_left.run_timed(time_sp=1046.801782, speed_sp=300, stop_action='hold')
            # wait till the motor has stopped
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            # release action
            motor_medium.run_timed(time_sp=3500, speed_sp=500, stop_action="brake")
            motor_medium.wait_while('running')
            sleep(2)

grab_the_blocks()
