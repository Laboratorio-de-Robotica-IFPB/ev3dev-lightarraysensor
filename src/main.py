#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.media.ev3dev import Font
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from mindsensorsPYB import LSA

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

lsa = LSA(Port.S3)

kP = 7
base_vel = 300

def control(sv):

    p = 8
    current = 0
    for i in range(4):
        current = (sv[i] * (-p) + sv[7-i] * p)
        p = p / 2
    
    current = current / (2*8 + 2*4 * 2*2 + 2)

    error = 0 - current

    return (kP * error), error

while True:

    buttons = ev3.buttons.pressed()
    sv = lsa.read_calibrated()
    
    if Button.UP in buttons:
        lsa.calibrate_white()
        wait(1000)
        print("White Limit is sucessfully calibrated")

    if Button.DOWN in buttons:
        lsa.calibrate_black()
        wait(1000)
        print("Black Limit is sucessfully calibrated")

    '''
    if sum(sv) < 5.0:
        ev3.speaker.beep()
        left_motor.stop()
        right_motor.stop()
        wait(1000)
    '''

    command, err = control(sv)
    
    left_motor.run(base_vel - command)
    right_motor.run(base_vel + command)


    #print("leitura do sensor: ", sv)
    print("erro: ", err)
    print("control command: ", command)