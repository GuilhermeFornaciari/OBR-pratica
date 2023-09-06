#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# iniciando motores garra

# inicando motores
motorEsquerdo = Motor(
    Port.A, positive_direction=Direction.CLOCKWISE, gears=None)
motorDireito = Motor(
    Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
# inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito,
                 wheel_diameter=33, axle_track=208.5)
# iniciando sensores de cor
sensorCorEsquerda = ColorSensor(Port.S1)
sensorCorDireita = ColorSensor(Port.S4)

# ev3
ev3 = EV3Brick()


while (True):
    x = sensorCorEsquerda.color()
    y = sensorCorDireita.color()

    print("cor esquerda = " + x)
    print("Cor direita = " + y)