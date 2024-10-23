#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
touch = TouchSensor(Port.S1)
motor = Motor(Port.A)
color = ColorSensor(Port.S2)

colorTuple = color.color()

print(colorTuple)