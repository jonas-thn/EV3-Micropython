#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from functions_color import *

#-------------GLOBAL DEVICES---------------#
ev3 = EV3Brick()
motorD = Motor(Port.D)
motorA = Motor(Port.A)
colorSens = ColorSensor(Port.S1)
gyro = GyroSensor(Port.S4)

#------------GLOBAL ATTRIBUTES--------------#
# color_values = {"GREEN": 90, "BLUE":-90, }

# scan_color_list = [Color.GREEN, Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.RED,
#                     Color.GREEN, Color.RED, Color.BLUE, Color.RED, Color.GREEN,
#                     Color.RED, Color.BLUE, Color.RED, Color.GREEN, Color.YELLOW]

scan_color_list = []

scan_speed = 150
move_speed = 500
turn_speed = 280
smooth_angle = 30
smooth_speed = 30
red_stop = 280
global_wait = 50
scan_delay = 315

#----------------START LOOP-----------------#
def start_loop():
    while(True):
        forward(motorA, motorD, scan_speed, scan_speed, gyro)

        wait(150)
        color = colorSens.color()
        if color == Color.GREEN:
            break
        elif (color == Color.BLUE) or (color == Color.BLACK):
            break
        elif color == Color.RED:
            break

#----------------SCAN LOOP------------------#
def scan_loop():
    while(True):
        forward(motorA, motorD, scan_speed, scan_speed, gyro)
        scan_color = colorSens.color()
        scan_color_list.append(scan_color)
        if (scan_color == Color.YELLOW):
            break
        wait(scan_delay)

# #-------------NAVIGATION LOOP---------------#
def navigation_loop():
    for i in range(len(scan_color_list)):
        color = scan_color_list.pop(0)

        if color == Color.RED:
            move_middle(motorA, motorD, colorSens, move_speed, 1, gyro, red_stop)
            wait(global_wait)

        elif color == Color.GREEN:
            # angle = color_values["GREEN"]
            right(turn_speed, gyro, motorD, motorA, 175, smooth_angle, smooth_speed)
            wait(global_wait)
            move_middle(motorA, motorD, colorSens, move_speed, 1, gyro, red_stop)
            wait(global_wait)

        elif (color == Color.BLUE) or (color == Color.BLACK):
            # angle = color_values["BLUE"]
            left(turn_speed, gyro, motorD, motorA, 175, smooth_angle, smooth_speed)
            wait(global_wait)
            move_middle(motorA, motorD, colorSens, move_speed, -1, gyro, red_stop)
            wait(global_wait)

        elif color == Color.YELLOW:
            stop(motorA, motorD)
            break

def main():
    start_loop()
    scan_loop()
    print(*scan_color_list)

    move_middle(motorA, motorD, colorSens, move_speed, 1, gyro, red_stop)
    wait(global_wait)

    navigation_loop()

if __name__ == "__main__":
    main()

    


