#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
motorD = Motor(Port.D)
motorA = Motor(Port.A)

motorA.run(100)
motorD.run(100)
wait(5000)
motorA.brake()
motorD.brake()