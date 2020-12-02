#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# Playing game of Tic-Tac-Toe
# Defining motors and sensors
motor_right = ev3.LargeMotor('outD')
motor_left = ev3.LargeMotor('outA')
motor_medium =ev3.MediumMotor('outC')
ts = ev3.TouchSensor()
cl = ev3.ColorSensor()

# to start the game, press the touch sensor once
# input either no colour or one random colour value
while not ts.value():
    sleep(0.01)

# movement functions
def rotate_180_right():
    # move motor right for 180 deg rotation
    motor_right.run_timed(time_sp=4131.368955, speed_sp=-100, stop_action='hold')
    motor_left.run_timed(time_sp=4131.368955, speed_sp=100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    sleep(0.3)

def rotate_180_left():
    # move motor left for 180 deg rotation
    motor_right.run_timed(time_sp=4131.368955, speed_sp=100, stop_action='hold')
    motor_left.run_timed(time_sp=4131.368955, speed_sp=-100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    sleep(0.3)

def rotate_90_left():
    # move motor left for 90 deg rotation
    motor_right.run_timed(time_sp=4187.207128, speed_sp=100, stop_action='hold')
    # wait till the motor has stopped
    motor_right.wait_while('running')
    sleep(0.3)

def rotate_90_reverse_left():
    # move motor left for 90 deg rotation
    motor_right.run_timed(time_sp=4187.207128, speed_sp=-100, stop_action='hold')
    # wait till the motor has stopped
    motor_right.wait_while('running')
    sleep(0.3)

def rotate_90_right():
    # move motor right for 90 deg rotation
    motor_left.run_timed(time_sp=4187.207128, speed_sp=100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    sleep(0.3)

def rotate_90_reverse_right():
    # move motor right for 90 deg rotation
    motor_left.run_timed(time_sp=4187.207128, speed_sp=-100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    sleep(0.3)

def rotate_90_left_alt():
    # move motor left for 90 deg rotation
    motor_right.run_timed(time_sp=2065.684478, speed_sp=100, stop_action='hold')
    motor_left.run_timed(time_sp=2065.684478, speed_sp=-100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    sleep(0.3)

def rotate_90_right_alt():
# move motor right for 90 deg rotation
    motor_right.run_timed(time_sp=2065.684478, speed_sp=-100, stop_action='hold')
    motor_left.run_timed(time_sp=2065.684478, speed_sp=100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    sleep(0.3)

def striaght_to_adj():
    motor_left.run_to_rel_pos(position_sp=442.5365854, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=442.5365854, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def reverse_to_adj():
    motor_left.run_to_rel_pos(position_sp=-442.5365854, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=-442.5365854, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def straight_1_adj():
    motor_left.run_to_rel_pos(position_sp=332, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=332, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def straight_1_middle():
    motor_left.run_to_rel_pos(position_sp=480, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=480, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def reverse_1_adj():
    motor_left.run_to_rel_pos(position_sp=-332, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=-332, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def reverse_1_middle():
    motor_left.run_to_rel_pos(position_sp=-480, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=-480, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(10)


def straight_2_adj():
    motor_left.run_to_rel_pos(position_sp=619.0243903, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=619.0243903, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def straight_2_middle():
    motor_left.run_to_rel_pos(position_sp=807.8048781, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=807.8048781, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(10)

def reverse_2_adj():
    motor_left.run_to_rel_pos(position_sp=-619.0243903, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=-619.0243903, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def reverse_2_middle():
    motor_left.run_to_rel_pos(position_sp=-807.8048781, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=-807.8048781, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(10)

def straight_3_adj():
    motor_left.run_to_rel_pos(position_sp=906.0487805, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=906.0487805, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def straight_3_middle():
    motor_left.run_to_rel_pos(position_sp=1135.609756, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=1135.609756, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def reverse_3_adj():
    motor_left.run_to_rel_pos(position_sp=-906.0487805, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=-906.0487805, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def reverse_3_middle():
    motor_left.run_to_rel_pos(position_sp=-1135.609756, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=-1135.609756, speed_sp=100, stop_action='hold')
    motor_right.wait_while('running')
    motor_left.wait_while('running')
    sleep(0.3)

def grab():
    # grab action
    motor_medium.run_timed(time_sp=3500, speed_sp=-1000, stop_action="brake")
    motor_medium.wait_while('running')
    sleep(0.1)

def release():
    # release action
    motor_medium.run_timed(time_sp=3500, speed_sp=1000, stop_action="brake")
    motor_medium.wait_while('running')
    sleep(10)


def game():
    for x in range(0,100):
        cl.mode = 'COL-REFLECT'
        x = cl.value()
        # first column of playing field
        if x == 1:
            rotate_180_right()
            grab()
            rotate_180_left()
            rotate_90_left_alt()
            striaght_to_adj()
            rotate_90_right()
            straight_3_adj()
            rotate_90_right()
            release()
            rotate_90_reverse_right()
            reverse_3_adj()
            rotate_90_reverse_right()
            reverse_to_adj()
            rotate_90_right_alt()
            sleep(10) #sleep for next colour detection
        if x == 4:
            rotate_180_right()
            grab()
            rotate_180_left()
            rotate_90_left_alt()
            striaght_to_adj()
            rotate_90_right()
            straight_2_adj()
            rotate_90_right()
            release()
            rotate_90_reverse_right()
            reverse_2_adj()
            rotate_90_reverse_right()
            reverse_to_adj()
            rotate_90_right_alt()
            sleep(10) #sleep for next colour detection
        if x == 7:
            rotate_180_right()
            grab()
            rotate_180_left()
            rotate_90_left_alt()
            striaght_to_adj()
            rotate_90_right()
            straight_1_adj()
            rotate_90_right()
            release()
            rotate_90_reverse_right()
            reverse_1_adj()
            rotate_90_reverse_right()
            reverse_to_adj()
            rotate_90_right_alt()
            sleep(10)  # sleep for next colour detection

        # third column of playing field
        if x == 3:
            rotate_180_right()
            grab()
            rotate_180_left()
            rotate_90_right_alt()
            striaght_to_adj()
            rotate_90_left()
            straight_3_adj()
            rotate_90_left()
            release()
            rotate_90_reverse_left()
            reverse_3_adj()
            rotate_90_reverse_left()
            reverse_to_adj()
            rotate_90_left_alt()
            sleep(10) #sleep for next colour detection
        if x == 6:
            rotate_180_right()
            grab()
            rotate_180_left()
            rotate_90_right_alt()
            striaght_to_adj()
            rotate_90_left()
            straight_2_adj()
            rotate_90_left()
            release()
            rotate_90_reverse_left()
            reverse_2_adj()
            rotate_90_reverse_left()
            reverse_to_adj()
            rotate_90_left_alt()
            sleep(10) #sleep for next colour detection
        if x == 9:
            rotate_180_right()
            grab()
            rotate_180_left()
            rotate_90_right_alt()
            striaght_to_adj()
            rotate_90_left()
            straight_1_adj()
            rotate_90_left()
            release()
            rotate_90_reverse_left()
            reverse_1_adj()
            rotate_90_reverse_left()
            reverse_to_adj()
            rotate_90_left_alt()
            sleep(10) #sleep for next colour detection

        # second column of playing field
        if x == 2:
            rotate_180_right()
            grab()
            rotate_180_left()
            straight_3_middle()
            release()
            reverse_3_middle()
        if x == 5:
            rotate_180_right()
            grab()
            rotate_180_left()
            straight_2_middle()
            release()
            reverse_2_middle()
        if x == 8:
            rotate_180_right()
            grab()
            rotate_180_left()
            straight_1_middle()
            release()
            reverse_1_middle()

game()
