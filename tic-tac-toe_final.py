#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

# Playing game of Tic-Tac-Toe
# Defining motors and sensors
motor_right = ev3.LargeMotor('outD')
motor_left = ev3.LargeMotor('outA')
motor_medium = ev3.MediumMotor('outB')
ts = ev3.TouchSensor()
cl = ev3.ColorSensor()

# to start the game, press the touch sensor once
# input either no colour or one random colour value
while not ts.value():
    sleep(0.01)


# movement functions
def rotate_180_right():
    # move motor right for 180 deg rotation
    motor_right.run_timed(time_sp=4189.368955, speed_sp=-100, stop_action='hold')
    motor_left.run_timed(time_sp=4189.368955, speed_sp=100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    sleep(0.3)


def rotate_180_left():
    # move motor left for 180 deg rotation
    motor_right.run_timed(time_sp=4189.368955, speed_sp=100, stop_action='hold')
    motor_left.run_timed(time_sp=4189.368955, speed_sp=-100, stop_action='hold')
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
    motor_right.run_timed(time_sp=2155.684478, speed_sp=100, stop_action='hold')
    motor_left.run_timed(time_sp=2155.684478, speed_sp=-100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    sleep(0.3)


def rotate_90_right_alt():
    # move motor right for 90 deg rotation
    motor_right.run_timed(time_sp=2175.684478, speed_sp=-100, stop_action='hold')
    motor_left.run_timed(time_sp=2175.684478, speed_sp=100, stop_action='hold')
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
    sleep(0.3)


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
    sleep(0.3)


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
    sleep(0.3)


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
    motor_left.run_to_rel_pos(position_sp=700, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=700, speed_sp=100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    sleep(0.1)
    motor_medium.run_timed(time_sp=3500, speed_sp=-1000, stop_action="brake")
    motor_medium.wait_while('running')
    sleep(0.1)
    motor_left.run_to_rel_pos(position_sp=-700, speed_sp=100, stop_action='hold')
    motor_right.run_to_rel_pos(position_sp=-700, speed_sp=100, stop_action='hold')
    # wait till the motor has stopped
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    sleep(0.1)


def release():
    # release action
    motor_medium.run_timed(time_sp=3500, speed_sp=1000, stop_action="brake")
    motor_medium.wait_while('running')
    sleep(0.1)


def space1():
    # put block on 1
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
    sleep(20)


def space2():
    # put block on 2
    rotate_180_right()
    grab()
    rotate_180_left()
    straight_3_middle()
    release()
    reverse_3_middle()
    sleep(20)


def space3():
    # put block on 3
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
    sleep(20)


def space4():
    # put block on 4
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
    sleep(20)


def space5():
    # put block on 5
    rotate_180_right()
    grab()
    rotate_180_left()
    straight_2_middle()
    release()
    reverse_2_middle()
    sleep(20)


def space6():
    # put block on 6
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
    sleep(20)


def space7():
    # put block on 7
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
    sleep(20)


def space8():
    # put block on 8
    rotate_180_right()
    grab()
    rotate_180_left()
    straight_1_middle()
    release()
    reverse_1_middle()
    sleep(20)


def space9():
    # put block on 9
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
    sleep(20)


def main():
    while ts.value() == 1:  # ts.value = 1
        ob = []  # opponent block
        for x in range(0, 100):
            cl.mode = 'COL-REFLECT'
            x = cl.value()
            if 30 <= x <= 35: # no colour (checked)
                ob.append(1)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
            if 0 <= x <= 4:  # brown checked
                ob.append(2)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
            if 4 <= x <= 6:  # black checked
                ob.append(3)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
            if 8 <= x <= 10:  # blue checked
                ob.append(4)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
            if 14 <= x <= 19:  # light green
                ob.append(5)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
            elif 40 <= x <= 48:  # coffeefilter checked
                ob.append(6)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
            if 80 <= x <= 89:  # yellow
                ob.append(7)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
            if 64 <= x <= 75:  #off-white checked
                ob.append(8)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()
            if x >= 90:  # white checked
                ob.append(9)
                if ob == [1]:  # going first
                    space1()
                elif ob == [1, 2] or ob == [1, 3] or ob == [1, 4] or ob == [1, 5] or ob == [1, 6] or ob == [1, 7] or ob == [1, 8]:
                    space9()
                elif ob == [1, 9]:
                    space3()
                elif ob == [1, 9, 2]:
                    space7()
                elif ob == [1, 9, 4] or ob == [1, 9, 5] or ob == [1, 9, 6] or ob == [1, 9, 7] or ob == [1, 9, 8]:  # win
                    space2()
                elif ob == [1, 5, 2] or ob == [1, 2, 5]:
                    space8()
                elif ob == [1, 5, 3] or ob == [1, 3, 5]:
                    space7()
                elif ob == [1, 5, 4] or ob == [1, 4, 5]:
                    space6()
                elif ob == [1, 5, 6] or ob == [1, 6, 5]:
                    space4()
                elif ob == [1, 5, 7] or ob == [1, 7, 5]:
                    space3()
                elif ob == [1, 5, 8] or ob == [1, 8, 5]:
                    space2()
                elif ob == [1, 2, 3] or ob == [1, 2, 4] or ob == [1, 2, 6] or ob == [1, 2, 7] or ob == [1, 2, 8] or ob == [1, 3, 2] or ob == [1, 3, 4] or ob == [1, 3, 6] or ob == [1, 3, 7] or ob == [1, 3, 8] or ob == [1, 4, 2] or ob == [1, 4, 3]  or ob == [1, 4, 6] or ob == [1, 4, 7] or ob == [1, 4, 8] or ob == [1, 6, 2] or ob == [1, 6, 3] or ob == [1, 6, 4] or ob == [1, 6, 7] or ob == [1, 6, 8] or ob == [1, 7, 2] or ob == [1, 7, 3] or ob == [1, 7, 4] or ob == [1, 7, 6] or ob == [1, 7, 8]  or ob == [1, 8, 2] or ob == [1, 8, 3] or ob == [1, 8, 4] or ob == [1, 8, 6] or ob == [1, 8, 7]: # win
                    space5()
                elif ob == [1, 9, 2, 4] or ob == [1, 2, 9, 4] or ob == [1, 9, 2, 6] or ob == [1, 2, 9, 6] or ob == [1, 9, 2, 8] or ob == [1, 2, 9, 8]:  # win
                    space5()
                elif ob == [1, 9, 2, 5] or ob == [1, 2, 9, 5]:  # win
                    space4()
                elif ob == [1, 5, 2, 7] or ob == [1, 2, 5, 7]:
                    space3()
                elif ob == [1, 5, 2, 3] or ob == [1, 5, 2, 4] or ob == [1, 5, 2, 6] or ob == [1, 2, 5, 3] or ob == [1, 2, 5, 4] or ob == [1, 2, 5, 6]:  # win
                    space7()
                elif ob == [1, 5, 3, 4] or ob == [1, 3, 5, 4] or ob == [1, 5, 3, 2] or ob == [1, 3, 5, 2] or ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space8()
                elif ob == [1, 5, 3, 8] or ob == [1, 3, 5, 8]:  # win
                    space4()
                elif ob == [1, 5, 4, 3] or ob == [1, 4, 5, 3]:
                    space7()
                elif ob == [1, 5, 4, 2] or ob == [1, 5, 4, 7] or ob == [1, 5, 4, 8] or ob == [1, 4, 5, 2] or ob == [1, 4, 5, 7] or ob == [1, 4, 5, 8]:  # win
                    space3()
                elif ob == [1, 5, 6, 7] or ob == [1, 6, 5, 7]:
                    space3()
                elif ob == [1, 5, 6, 2] or ob == [1, 5, 6, 3] or ob == [1, 5, 6, 8] or ob == [1, 6, 5, 2] or ob == [1, 6, 5, 3] or ob == [1, 6, 5, 8]:  # win
                    space7()
                elif ob == [1, 5, 7, 2] or ob == [1, 7, 5, 2] or ob == [1, 5, 7, 4] or ob == [1, 7, 5, 4] or ob == [1, 5, 7, 8] or ob == [1, 7, 5, 8]:  # win
                    space6()
                elif ob == [1, 5, 7, 6] or ob == [1, 7, 5, 6]:  # win
                    space2()
                elif ob == [1, 5, 8, 3] or ob == [1, 8, 5, 3]:
                    space7()
                elif ob == [1, 5, 8, 4] or ob == [1, 5, 8, 6] or ob == [1, 5, 8, 7] or ob == [1, 8, 5, 4] or ob == [1, 8, 5, 6] or ob == [1, 8, 5, 7]:  # win
                    space3()
                elif ob == [1, 5, 2, 7, 6] or ob == [1, 2, 5, 7, 6]:  # tie
                    space4()
                elif ob == [1, 5, 2, 7, 4] or ob == [1, 2, 5, 7, 4]:  # win
                    space6()
                elif ob == [1, 5, 4, 3, 2] or ob == [1, 4, 5, 3, 2]:  # win
                    space8()
                elif ob == [1, 5, 4, 3, 8] or ob == [1, 4, 5, 3, 8]:  # tie
                    space2()
                elif ob == [1, 5, 6, 7, 2] or ob == [1, 6, 5, 7, 2]:  # tie
                    space8()
                elif ob == [1, 5, 6, 7, 8] or ob == [1, 6, 5, 7, 8]:  # win
                    space2()
                elif ob == [1, 5, 8, 7, 4] or ob == [1, 8, 5, 7, 4]:  # tie
                    space6()
                elif ob == [1, 5, 8, 7, 6] or ob == [1, 8, 5, 7, 6]:  # win
                    space4()
                elif ob == [5]:  # going second + opp first on 5
                    space1()
                elif ob == [5, 2]:
                    space8()
                elif ob == [5, 3]:
                    space7()
                elif ob == [5, 4]:
                    space6()
                elif ob == [5, 6]:
                    space4()
                elif ob == [5, 7]:
                    space3()
                elif ob == [5, 8]:
                    space2()
                elif ob == [5, 9]:
                    space3()
                elif ob == [5, 2, 3]:
                    space7()
                elif ob == [5, 2, 4]:
                    space6()
                elif ob == [5, 2, 6]:
                    space4()
                elif ob == [5, 2, 7]:
                    space3()
                elif ob == [5, 2, 9]:
                    space4()
                elif ob == [5, 3, 4]:
                    space6()
                elif ob == [5, 3, 2] or ob == [5, 3, 6] or ob == [5, 3, 8] or ob == [5, 3, 9]:  # win
                    space4()
                elif ob == [5, 4, 2]:
                    space8()
                elif ob == [5, 4, 3]:
                    space7()
                elif ob == [5, 4, 7]:
                    space3()
                elif ob == [5, 4, 8]:
                    space2()
                elif ob == [5, 4, 9]:
                    space3()
                elif ob == [5, 6, 7]:
                    space3()
                elif ob == [5, 6, 2] or ob == [5, 6, 3] or ob == [5, 6, 8] or ob == [5, 6, 9]:  # win
                    space7()
                elif ob == [5, 7, 2]:
                    space8()
                elif ob == [5, 7, 4] or ob == [5, 7, 6] or ob == [5, 7, 8] or ob == [5, 7, 9]:  # win
                    space2()
                elif ob == [5, 8, 3]:
                    space7()
                elif ob == [5, 8, 4] or ob == [5, 8, 6] or ob == [5, 8, 7] or ob == [5, 8, 9]:  # win
                    space3()
                elif ob == [5, 9, 2]:
                    space8()
                elif ob == [5, 9, 4] or ob == [5, 9, 6] or ob == [5, 9, 7] or ob == [5, 9, 8]:  # win
                    space2()
                elif ob == [5, 2, 3, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 3, 4] or ob == [5, 2, 3, 6]:  # win
                    space9()
                elif ob == [5, 2, 4, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 2, 4, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 4, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 2, 6, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 2, 6, 3] or ob == [5, 2, 6, 9]:  # win
                    space7()
                elif ob == [5, 2, 7, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 2, 7, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 2, 7, 9]:  # opp4 tie
                    space6()
                elif ob == [5, 2, 9, 7]:  # opp6 tie
                    space3()
                elif ob == [5, 2, 9, 3] or ob == [5, 2, 9, 6]:  # win
                    space7()
                elif ob == [5, 3, 4, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 3, 4, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 3, 4, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 2, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 2, 7]:  # opp9 tie
                    space3()
                elif ob == [5, 4, 2, 9]:  # opp3 tie
                    space7()
                elif ob == [5, 4, 3, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 4, 3, 8]:  # opp9 tie
                    space2()
                elif ob == [5, 4, 3, 9]:  # opp2 tie
                    space7()
                elif ob == [5, 4, 7, 9]:  # opp2 tie
                    space8()
                elif ob == [5, 4, 7, 2] or ob == [5, 4, 7, 8]:  # win
                    space9()
                elif ob == [5, 4, 8, 3]:  # opp9 tie
                    space7()
                elif ob == [5, 4, 8, 7] or ob == [5, 4, 8, 9]:  # win
                    space3()
                elif ob == [5, 4, 9, 2]:  # opp7 tie
                    space8()
                elif ob == [5, 4, 9, 7] or ob == [5, 4, 9, 8]:  # win
                    space2()
                elif ob == [5, 6, 7, 2]:  # opp9 tie
                    space8()
                elif ob == [5, 6, 7, 8] or ob == [5, 6, 7, 9]:  # win
                    space2()
                elif ob == [5, 7, 2, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 7, 2, 6]:  # opp9 tie
                    space4()
                elif ob == [5, 7, 2, 9]:  # opp6 tie
                    space4()
                elif ob == [5, 8, 3, 4]:  # opp9 tie
                    space6()
                elif ob == [5, 8, 3, 6] or ob == [5, 8, 3, 9]:  # win
                    space4()
                elif ob == [5, 9, 2, 4]:  # opp7 tie
                    space6()
                elif ob == [5, 9, 2, 6]:  # opp7 tie
                    space4()
                elif ob == [5, 9, 2, 7]:  # opp6 tie
                    space4()
                elif ob == [2] or ob == [3] or ob == [4] or ob == [6] or ob == [7] or ob == [8] or ob == [9]:  # strategy 2 (not in the midde)
                    space5()
                elif ob == [2, 1] or ob == [6, 9] or ob == [9, 6] or ob == [2, 6] or ob == [6, 2] or ob == [2, 9] or ob == [9, 2] or ob == [6, 9] or ob == [9, 6] or ob == [6, 1]:
                    space3()
                elif ob == [2, 3] or ob == [3, 2] or ob == [4, 7] or ob == [7, 4] or ob == [2, 7] or ob == [7, 2] or ob == [2, 4] or ob == [4, 2] or ob == [2, 8] or ob == [8, 2] or ob == [3, 4] or ob == [4, 3]:
                    space1()
                elif ob == [3, 1] or ob == [5, 1] or ob == [9, 1] or ob == [8, 1] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6] or ob == [3, 8] or ob == [8, 3] or ob == [3, 7] or ob == [7, 3] or ob == [3, 4] or ob == [4, 3]:
                    space2()
                elif ob == [7, 1]:
                    space4()
                elif ob == [3, 9] or ob == [9, 3]:
                    space6()
                elif ob == [8, 9] or ob == [9, 8] or ob == [4, 1] or ob == [4, 8] or ob == [8, 4] or ob == [4, 9] or ob == [9, 4]:
                    space7()
                elif ob == [7, 9] or ob == [9, 7] or ob == [2, 9] or ob == [9, 2] or ob == [3, 7] or ob == [7, 3] or ob == [4, 6] or ob == [6, 4] or ob == [9, 1]:
                    space8()
                elif ob == [3, 6] or ob == [6, 3] or ob == [3, 8] or ob == [8, 3] or ob == [7, 8] or ob == [8, 7] or ob == [6, 7] or ob == [7, 6] or ob == [6, 8] or ob == [8, 6]:
                    space9()
                elif ob == [2, 1, 7]:
                    space2()
                elif ob == [2, 3, 9] or ob == [3, 2, 9]:
                    space6()
                elif ob == [2, 4, 9] or ob == [4, 2, 9]:
                    space7()
                elif ob == [2, 6, 7] or ob == [6, 2, 7]:
                    space9()
                elif ob == [2, 7, 9] or ob == [7, 2, 9]:
                    space8()
                elif ob == [2, 8, 9] or ob == [8, 2, 9]:
                    space7()
                elif ob == [2, 9, 7] or ob == [9, 2, 7]:
                    space8()
                elif ob == [3, 1, 8]:
                    space4()
                elif ob == [3, 5, 9] or ob == [5, 3, 9]:
                    space6()
                elif ob == [3, 4, 9] or ob == [4, 3, 9]:
                    space6()
                elif ob == [3, 6, 1] or ob == [6, 3, 1]:
                    space2()
                elif ob == [3, 7, 2] or ob == [7, 3, 2]:
                    space1()
                elif ob == [3, 8, 1] or ob == [8, 3, 1]:
                    space2()
                elif ob == [3, 9, 4] or ob == [9, 3, 4]:
                    space8()
                elif ob == [4, 1, 3]:
                    space2()
                elif ob == [4, 6, 9] or ob == [6, 4, 9]:
                    space8()
                elif ob == [4, 7, 9] or ob == [7, 4, 9]:
                    space8()
                elif ob == [4, 8, 3] or ob == [8, 4, 3]:
                    space1()
                elif ob == [4, 9, 3] or ob == [9, 4, 3]:
                    space6()
                elif ob == [6, 1, 7]:
                    space4()
                elif ob == [6, 7, 1] or ob == [7, 6, 1]:
                    space4()
                elif ob == [6, 8, 1] or ob == [8, 6, 1]:
                    space3()
                elif ob == [6, 9, 7] or ob == [9, 6, 7]:
                    space8()
                elif ob == [7, 1, 6]:
                    space8()
                elif ob == [7, 8, 1] or ob == [8, 7, 1]:
                    space4()
                elif ob == [7, 9, 2] or ob == [9, 7, 2]:
                    space4()
                elif ob == [8, 1, 3]:
                    space2()
                elif ob == [8, 9, 3] or ob == [9, 8, 3]:
                    space6()
                elif ob == [9, 1, 2]:
                    space3()
                elif ob == [2, 1, 7, 6] or ob == [2, 3, 9, 4] or ob == [3, 2, 9, 4]:
                    space8()
                elif ob == [2, 4, 9, 3] or ob == [4, 2, 9, 3] or ob == [2, 7, 9, 4] or ob == [7, 2, 9, 4] or ob == [2, 7, 9, 3] or ob == [7, 2, 9, 3]:
                    space6()
                elif ob == [2, 6, 7, 1] or ob == [6, 2, 7, 1] or ob == [2, 8, 9, 3] or ob == [8, 2, 9, 3] or ob == [2, 7, 9, 1] or ob == [9, 2, 7, 1] or ob == [2, 9, 7, 6] or ob == [9, 2, 7, 6]:
                    space4()
                elif ob == [2, 7, 9, 6] or ob == [7, 2, 9, 6] or ob == [2, 8, 9, 4] or ob == [8, 2, 9, 4]:
                    space3()
                elif ob == [2, 9, 7, 4] or ob == [9, 2, 7, 4]:
                    space1()
                elif ob == [3, 1, 8, 6]:
                    space9()
                elif ob == [3, 4, 9, 2] or ob == [4, 3, 9, 2] or ob == [3, 4, 9, 7] or ob == [4, 3, 9, 7]:
                    space8()
                elif ob == [3, 4, 9, 8] or ob == [4, 3, 9, 8] or ob == [3, 6, 1, 8] or ob == [6, 3, 1, 8] or ob == [3, 8, 1, 4] or ob == [8, 3, 1, 4] or ob == [3, 8, 1, 6] or ob == [8, 3, 1, 6]:
                    space7()
                elif ob == [3, 7, 2, 9] or ob == [7, 3, 2, 9]:
                    space6()
                elif ob == [3, 8, 1, 7] or ob == [8, 3, 1, 7]:
                    space4()
                elif ob == [3, 9, 4, 2] or ob == [9, 3, 4, 2]:
                    space1()
                elif ob == [4, 1, 3, 8]:
                    space9()
                elif ob == [4, 6, 2, 9] or ob == [6, 4, 2, 9]:
                    space3()
                elif ob == [4, 7, 9, 2] or ob == [7, 4, 9, 2] or ob == [4, 8, 3, 9] or ob == [8, 4, 3, 9]:
                    space6()
                elif ob == [4, 9, 3, 1] or ob == [9, 4, 3, 1]:
                    space2()
                elif ob == [4, 9, 3, 2] or ob == [9, 4, 3, 2] or ob == [4, 9, 3, 8] or ob == [9, 4, 3, 8]:
                    space1()
                elif ob == [6, 1, 7, 2] or ob == [6, 1, 7, 9]:
                    space8()
                elif ob == [6, 1, 7, 8]:
                    space9()
                elif ob == [6, 7, 1, 2] or ob == [7, 6, 1, 2] or ob == [6, 7, 1, 8] or ob == [7, 6, 1, 8]:
                    space3()
                elif ob == [6, 7, 1, 3] or ob == [7, 6, 1, 3]:
                    space2()
                elif ob == [6, 8, 1, 7] or ob == [8, 6, 1, 7] or ob == [6, 9, 7, 2] or ob == [9, 6, 7, 2]:
                    space4()
                elif ob == [7, 1, 6, 2] or ob == [7, 8, 1, 6] or ob == [8, 7, 1, 6] or ob == [7, 9, 2, 6] or ob == [9, 7, 2, 6]:
                    space3()
                elif ob == [8, 1, 3, 4] or ob == [8, 1, 3, 6]:
                    space9()
                elif ob == [8, 1, 3, 9]:
                    space6()
                elif ob == [8, 9, 3, 4] or ob == [9, 8, 3, 4]:
                    space1()
                elif ob == [9, 1, 2, 7]:
                    space6()

if __name__ == "__main__":
    main()