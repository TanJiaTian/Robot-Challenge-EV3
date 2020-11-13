#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# making a loop square (task 1)

# Connect the output B to the motorotor_left = ev3.LargeMotor('outB')
motor_right = ev3.LargeMotor('outC')
motor_left = ev3.LargeMotor('outB')
# move motor on both sides for 1500ms with 500deg/sec
motor_left.run_timed(time_sp=1500, speed_sp=500)
motor_right.run_timed(time_sp=1500, speed_sp=500)
# wait till the motor has stopped
motor_right.wait_while('running')
motor_left.wait_while('running')
# move motor right for 90 deg
motor_right.run_timed(time_sp=3000, speed_sp=151.348)
# motor right stopped
motor_right.wait_while('running')
# move motor on both sides for 1500ms with 500deg/sec
motor_left.run_timed(time_sp=1500, speed_sp=500)
motor_right.run_timed(time_sp=1500, speed_sp=500)
# wait till the motor has stopped
motor_right.wait_while('running')
motor_left.wait_while('running')
# move motor right for 90 deg
motor_left.run_timed(time_sp=3000, speed_sp=151.348)
# motor right stopped
motor_left.wait_while('running')
# move motor on both sides for 1500ms with 500deg/sec
motor_left.run_timed(time_sp=3770, speed_sp=500)
motor_right.run_timed(time_sp=3770, speed_sp=500)
# wait till the motor has stopped
motor_right.wait_while('running')
motor_left.wait_while('running')
# move motor right for 90 deg
motor_left.run_timed(time_sp=3000, speed_sp=151.348)
# motor right stopped
motor_left.wait_while('running')
# move motor on both sides for 1500ms with 500deg/sec
motor_left.run_timed(time_sp=3770, speed_sp=500)
motor_right.run_timed(time_sp=3770, speed_sp=500)
# wait till the motor has stopped
motor_right.wait_while('running')
motor_left.wait_while('running')
# move motor right for 90 deg
motor_left.run_timed(time_sp=3000, speed_sp=151.348)
# motor right stopped
motor_left.wait_while('running')
# move motor on both sides for 1500ms with 500deg/sec
motor_left.run_timed(time_sp=3770, speed_sp=500)
motor_right.run_timed(time_sp=3770, speed_sp=500)
# wait till the motor has stopped
motor_right.wait_while('running')
motor_left.wait_while('running')
# move motor right for 90 deg
motor_left.run_timed(time_sp=3000, speed_sp=151.348)
# motor right stopped
motor_left.wait_while('running')
motor_left.run_timed(time_sp=1500, speed_sp=500)
motor_right.run_timed(time_sp=1500, speed_sp=500)
# wait till the motor has stopped
motor_right.wait_while('running')
motor_left.wait_while('running')
# move motor right for 90 deg
motor_right.run_timed(time_sp=3000, speed_sp=151.348)
# motor right stopped
motor_right.wait_while('running')
# move motor on both sides for 1500ms with 500deg/sec
motor_left.run_timed(time_sp=1500, speed_sp=500)
motor_right.run_timed(time_sp=1500, speed_sp=500)
# wait till the motor has stopped
motor_right.wait_while('running')
motor_left.wait_while('running')
ev3.Sound.speak("Hello I am Karen I am the only boss in Tick-Tack-Toe")
sleep(8)






