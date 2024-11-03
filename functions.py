from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

global_angle = 0

def forward(motorA, motorD, speedA, speedD, gyro):
    global global_angle
    motorD.run(speedD - 10*(gyro.angle()-global_angle))
    motorA.run(speedA + 10*(gyro.angle()-global_angle))

def stop(motorA, motorD):
    motorA.brake()
    motorD.brake()

def move_middle(motorA, motorD, colorSens, move_speed, invert, gyro, _red_stop_delay):
    a_speed = move_speed
    d_speed = move_speed
    offset = 0

    red_stop_delay = _red_stop_delay

    while(True):
        forward(motorA, motorD, a_speed, d_speed, gyro)
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

# def right_turn(gyro, motorA, motorD, turn_speed, dest_angle):
#     if turn_speed > 0:
#         while(gyro.angle() < dest_angle):
#             motorA.run(-turn_speed)
#             motorD.run(turn_speed)

#         motorA.hold()
#         motorD.hold()

#         if gyro.angle() > dest_angle:
#             left_turn(gyro, motorA, motorD, turn_speed/4, dest_angle)
#         else:
#             correct_gyro(motorA, motorD, gyro.angle(), dest_angle, turn_speed/5)
#             gyro.reset_angle(0)

# def left_turn(gyro, motorA, motorD, turn_speed, dest_angle):
#     if turn_speed > 0:
#         while(gyro.angle() > dest_angle):
#             motorA.run(turn_speed)
#             motorD.run(-turn_speed)

#         motorA.hold()
#         motorD.hold()

#         if gyro.angle() < -89:
#             right_turn(gyro, motorA, motorD, turn_speed/4, dest_angle)
#         else:
#             correct_gyro(motorA, motorD, gyro.angle(), dest_angle, turn_speed/5)

#             gyro.reset_angle(0)

# def correct_gyro(motorA, motorD, current_angle, desired_angle, turn_speed):
#     if(current_angle == desired_angle):
#         pass

#     elif(current_angle > desired_angle):
#         while(current_angle > desired_angle):
#             motorA.run(turn_speed)
#             motorD.run(-turn_speed)
#         stop(motorA, motorD)

#     elif(current_angle < desired_angle):
#         while(current_angle > desired_angle):
#             motorA.run(-turn_speed)
#             motorD.run(turn_speed)
#         stop(motorA, motorD)

#     wait(100)

def left(speed, gyro, motorD, motorA, wait_seconds, angle_smooth, smooth_speed):
    global global_angle 
    global_angle -= 90
    wait(wait_seconds)
    motorD.run(-speed)
    motorA.run(speed)
    while(gyro.angle() > global_angle+angle_smooth):
        pass
    motorD.run(-smooth_speed)
    motorA.run(smooth_speed)
    while(gyro.angle() > global_angle):
        pass
    motorA.hold()
    motorD.hold()
    wait(wait_seconds)


def right(speed, gyro, motorD, motorA, wait_seconds, angle_smooth, smooth_speed):
    global global_angle
    global_angle += 90
    wait(wait_seconds)
    motorD.run(speed)
    motorA.run(-speed)
    while(gyro.angle() < global_angle-angle_smooth):
        pass
    motorD.run(smooth_speed)
    motorA.run(-smooth_speed)
    while(gyro.angle() < global_angle):
        pass
    motorA.hold()
    motorD.hold()
    wait(wait_seconds)

