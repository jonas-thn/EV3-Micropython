import math
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

if __name__ == "__main__":
    raise SystemExit("Wrong file!")

global_angle = 0
first = True
first_dead_end = True

def look_around(head_rotation_angle, ultra_sens, distance_side, motorHead, move_spped, turn_speed, smooth_speed, block, gyro, motorD, motroA, global_wait):
    global first
    motorHead.run_angle(head_rotation_angle, -90)
    motorHead.hold()
    dis_l = ultra_sens.distance()

    if(dis_l > distance_side + 80):
        motorHead.run_angle(head_rotation_angle, 90)
        motorHead.hold()
        left(turn_speed, gyro, motorD, motroA, global_wait)
        first = True
        motorD.reset_angle(0)
    else:
        motorHead.run_angle(head_rotation_angle, 180)
        motorHead.hold()
        dis_r = ultra_sens.distance()
        if(dis_r > distance_side + 80):
            motorHead.run_angle(head_rotation_angle, -90)
            first = False
            right(turn_speed, gyro, motorD, motroA, global_wait)
        else:
            motorHead.run_angle(head_rotation_angle, -90)
            backwards(turn_speed, gyro, motorD, motroA, global_wait)
            if (first == False):
                
                motorD.reset_angle(0)
                motroA.reset_angle(0)
                motroA.run_target(move_spped, block-15, wait=False)
                motorD.run_target(move_spped, block-15, wait=True)
                motroA.run_target(2*smooth_speed, block, wait=False)
                motorD.run_target(2*smooth_speed, block, wait=True)
                motorD.hold()
                motroA.hold()

                look_right(head_rotation_angle, ultra_sens, distance_side, motorHead, move_spped, turn_speed, smooth_speed, block, gyro, motorD, motroA, global_wait)
            elif(first == True):
                first = False

def look_right(head_rotation_angle, ultraSensor, distance_side, motorHead, move_speed, turn_speed, smooth_speed, block, gyro, motorD, motorA, global_wait):
    global first
    motorHead.run_angle(head_rotation_angle, 90)
    motorHead.hold()
    dis_r = ultraSensor.distance()
    motorHead.run_angle(head_rotation_angle, -90)
    motorHead.hold()
    if(dis_r > distance_side+ + 80):
        right(turn_speed, gyro, motorD, motorA, global_wait)
    else:
        left(turn_speed, gyro, motorD, motorA, global_wait)
        

def left(turn_speed, gyro, motorD, motorA, global_wait):
    global global_angle 
    global_angle -= 90
    wait(global_wait)
    motorD.run(-turn_speed)
    motorA.run(turn_speed)
    while(gyro.angle() > global_angle+30):
        pass
    motorD.run(-30)
    motorA.run(30)
    while(gyro.angle() > global_angle):
        pass
    motorA.hold()
    motorD.hold()
    wait(global_wait)


def right(turn_speed, gyro, motorD, motorA, global_wait):
    global global_angle
    global_angle += 90
    wait(global_wait)
    motorD.run(turn_speed)
    motorA.run(-turn_speed)
    while(gyro.angle() < global_angle-30):
        pass
    motorD.run(30)
    motorA.run(-30)
    while(gyro.angle() < global_angle):
        pass
    motorA.hold()
    motorD.hold()
    wait(global_wait)

def backwards(turn_speed, gyro, motorD, motorA, global_Wait):
    global global_angle
    global_angle += 180
    wait(global_Wait)
    motorD.run(turn_speed)
    motorA.run(-turn_speed)
    while(gyro.angle() < global_angle-26):
        pass
    motorD.run(20)
    motorA.run(-20)
    while(gyro.angle() < global_angle):
        pass
    motorA.hold()
    motorD.hold()
    wait(global_Wait)

def forward(ultraSens, motorD, motroA, move_spped, distance_front, gyro):
    global global_angle
    global first
    if (ultraSens.distance() > (distance_front + 20)):
        motorD.run(move_spped - 10*(gyro.angle()-global_angle))
        motroA.run(move_spped + 10*(gyro.angle()-global_angle))
    if(first == True):
        if(motorD.angle() > 700):
            first = False

def set_first_false():
    global first
    first = False



    