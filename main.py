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
color_values = {"GREEN": 90, "RED": 0, "BLUE":-90, "YELLOW": "END" }
scan_color_list = []

#----------------SCAN LOOP------------------#
while(True):
    forward(motorA, motorD, scan_speed)
    scan_color = colorSens.color()
    scan_color_list.append(colorSens.color())
    print()
    if (scan_color == None):
        stop(motorA, motorD)
        print(scan_color_list)

        break
    wait(300)

