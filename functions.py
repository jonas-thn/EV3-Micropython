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

def move_middle(motorA, motorD, colorSens, move_speed, invert):
    a_speed = move_speed
    d_speed = move_speed
    offset = 25

    red_stop_delay = 250

    while(True):
        forward(motorA, motorD, a_speed, d_speed)
        scan_rgb = colorSens.rgb()
        average = (scan_rgb[0] + scan_rgb[1] + scan_rgb[2]) / 3
        if(average > 60):
            d_speed = move_speed - 2*offset * invert
        elif(average > 40):
            d_speed = move_speed - offset * invert
        elif(average < 20):
            a_speed = move_speed - offset * invert
        else:
            a_speed = move_speed
            d_speed = move_speed

        if(colorSens.color() == Color.RED):
            wait(red_stop_delay)
            stop(motorA, motorD)
            break
        wait(50)

def right_turn(gyro, motorA, motorD, turn_speed, dest_angle):
    if turn_speed > 0:
        while(gyro.angle() < dest_angle):
            motorA.run(-turn_speed)
            motorD.run(turn_speed)

        motorA.hold()
        motorD.hold()

        print(gyro.angle())

        if gyro.angle() > 91:
            left_turn(gyro, motorA, motorD, turn_speed/4, dest_angle)
        else:
            gyro.reset_angle(0)

def left_turn(gyro, motorA, motorD, turn_speed, dest_angle):
    if turn_speed > 0:
        while(gyro.angle() > dest_angle):
            motorA.run(turn_speed)
            motorD.run(-turn_speed)

        motorA.hold()
        motorD.hold()

        print(gyro.angle())

        if gyro.angle() < -91:
            right_turn(gyro, motorA, motorD, turn_speed/4, dest_angle)
        else:
            gyro.reset_angle(0)


