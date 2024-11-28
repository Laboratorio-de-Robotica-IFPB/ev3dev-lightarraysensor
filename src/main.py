#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.media.ev3dev import Font
from pybricks.tools import wait
from mindsensorsPYB import LightSensorArray

font = Font(size=6)

ev3 = EV3Brick()
ev3.screen.set_font(font)

lsa = LightSensorArray(Port.S4)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

while True:

    sv = lsa.get_raw_voltages()
    
    if sv is None:
        print("WARNING: os dados do sensor são inválidos ou None.")
    else:
        print(sv)

        print("handling data:", (sv[2] * sv[7])/ 4 * sv[5]) 

'''
while True:
    buttons = ev3.buttons.pressed()
    sv = lsa.read_calibrated()
    
    if Button.UP in buttons:
        lsa.issueCommand('W')
        wait(1000)
        print("White Limit is sucessfully calibrated")

    if Button.DOWN in buttons:
        lsa.issueCommand('B')
        wait(1000)
        print("Black Limit is sucessfully calibrated")

    print("leitura do sensor: ", sv)

    left_motor.run(300)
    right_motor.run(300)
    
    if sv == bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00'):
        ev3.speaker.beep()
        left_motor.stop()
        right_motor.stop()
        wait(1000)
    
'''