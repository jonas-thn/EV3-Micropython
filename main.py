#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from functions import *

#-------------GLOBAL DEVICES---------------#
ev3 = EV3Brick()
motorD = Motor(Port.D)
motorA = Motor(Port.A)
colorSens = ColorSensor(Port.S1)
gyro = GyroSensor(Port.S4)

#------------GLOBAL ATTRIBUTES--------------#
scan_speed = 150
#right = 90, left = -90
color_values = {"GREEN": 90, "BLUE":-90, }
# scan_color_list = [Color.GREEN, Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.RED,
#                     Color.GREEN, Color.RED, Color.BLUE, Color.RED, Color.GREEN,
#                     Color.RED, Color.BLUE, Color.RED, Color.GREEN, Color.YELLOW]
scan_color_list = []

move_speed = 400
turn_speed = 200

while(True):
    forward(motorA, motorD, scan_speed, scan_speed, gyro)

    wait(150)
    color = colorSens.color()
    if color == Color.GREEN:
        break
    # elif color == Color.BLUE:
    #     break
    # elif color == Color.RED:
    #     break

#----------------SCAN LOOP------------------#
while(True):
    forward(motorA, motorD, scan_speed, scan_speed, gyro)
    scan_color = colorSens.color()
    scan_color_list.append(colorSens.color())
    if (scan_color == Color.YELLOW):
        break
    wait(315)

move_middle(motorA, motorD, colorSens, move_speed, 1, gyro)
wait(100)
print(scan_color_list)

# #-------------NAVIGATION LOOP---------------#
for i in range(len(scan_color_list)):
    color = scan_color_list.pop(0)

    if color == Color.RED:
        move_middle(motorA, motorD, colorSens, move_speed, 1, gyro)
        wait(100)

    elif color == Color.GREEN:
        # angle = color_values["GREEN"]
        right(turn_speed, gyro, motorD, motorA, 175, 30, 30)
        wait(100)
        move_middle(motorA, motorD, colorSens, move_speed, 1, gyro)
        wait(100)

    elif color == Color.BLUE or color == Color.BLACK:
        # angle = color_values["BLUE"]
        left(turn_speed, gyro, motorD, motorA, 175, 30, 30)
        wait(100)
        move_middle(motorA, motorD, colorSens, move_speed, -1, gyro)
        wait(100)

    elif color == Color.YELLOW:
        stop(motorA, motorD)
        break

    


