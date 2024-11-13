#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks.messaging import BluetoothMailboxServer, LogicMailbox
from pybricks.media.ev3dev import Image, ImageFile
from funktionen_labyrinth import *

ev3 = EV3Brick()
gyro = GyroSensor(Port.S1, Direction.CLOCKWISE)
ultraSens = UltrasonicSensor(Port.S4)
motorD = Motor(Port.D)
motroA = Motor(Port.A)
motorHead = Motor(Port.C)

distance_front = 160
distance_side = 130

move_spped = 575
turn_speed = 350
smooth_speed = 20
global_wait = 175
head_rotation_speed = 1000

block = 655

def start():
    gyro.reset_angle(0)

    motorHead.run_angle(head_rotation_speed, 180)
    motorHead.hold
    wait(global_wait)
    dis_h = ultraSens.distance()
    while(dis_h - ultraSens.distance() <= 8):
        pass
    motorHead.run_angle(head_rotation_speed, -180)
    motorHead.hold()
    wait(global_wait)

    if (ultraSens.distance() > distance_front +40):
        set_first_false()

def loop():
    while(True):
        wait(10)
        forward(ultraSens, motorD, motroA, move_spped, distance_front, gyro)

        if(ultraSens.distance() < distance_front):
            motorD.brake()
            motroA.brake()
            wait(10)
            motorD.brake()
            motroA.brake()
            look_around(head_rotation_speed, ultraSens, distance_side, motorHead, move_spped, turn_speed, smooth_speed, block, gyro, motorD, motroA, global_wait)
            
def main():
    start()
    loop()

if __name__ == "__main__":
    main()








    