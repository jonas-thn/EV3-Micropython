from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

def forward(motorA, motorD, speedA, speedD):
    motorA.run(speedA)
    motorD.run(speedD)

def stop(motorA, motorD):
    motorA.brake()
    motorD.brake()

def move_middle(motorA, motorD, colorSens, move_speed):
    #----------------MOVE LOOP------------------#
    a_speed = move_speed
    d_speed = move_speed
    offset = 25

    while(True):
        forward(motorA, motorD, a_speed, d_speed)
        scan_rgb = colorSens.rgb()
        average = (scan_rgb[0] + scan_rgb[1] + scan_rgb[2]) / 3
        print(average)
        if(average > 40):
            d_speed = move_speed - offset
        elif(average < 20):
            a_speed = move_speed - offset
        else:
            a_speed = move_speed
            d_speed = move_speed

        if(colorSens.color() == Color.RED):
            stop(motorA, motorD)
            break
        wait(5)