#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.media.ev3dev import Font
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from mindsensorsPYB import LSA


ev3 = EV3brick()
lsa = LSA(Port.S4)

vel_base = 100
erro = 0
erro_anterior = 0
erro_total = 0

kp = 1
ki = 1
kd = 1

def pegaErro(array_sensores):
    array_tratado[8]

    for sensor in array_sensores:
        array_tratado[sensor] = 0xFF - array_sensores[sensor]
    erro_calculado = 0
    pos = 0
    for i in range(-4,5):
        if i != 0:
            erro_calculado += i*array_tratado[i]
            pos += 1

    return erro  


while True:
    sv = lsa.read_calibrated()
    erro_anterior = erro
    erro_total += erro
    erro = pegaErro(sv)

    proporcional = kp*erro
    integral = ki*erro_total
    derivada = kd*(erro - erro_anterior) 

    print("Proporcional: " proporcional "Integral: ", integral "Derivada: ",derivada)
    #vel_dir = vel_base + proporcional + integral + derivada
