from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

def forward(motorA, motorD, speed):
    motorA.run(speed)
    motorD.run(speed)

def stop(motorA, motorD):
    motorA.brake()
    motorD.brake()