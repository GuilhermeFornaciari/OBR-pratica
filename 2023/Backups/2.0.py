#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
# Create your objects here.#inicando motores
motorEsquerdo = Motor(
    Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=None)
motorDireito = Motor(
    Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=None)
# inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito,
                 wheel_diameter=32.8, axle_track=218)
# iniciando sensores de cor
CorEsquerda = ColorSensor(Port.S1)
CorDireita = ColorSensor(Port.S2)


def pretos(lado, sensor1, sensor2):
    robo.straight(20)
    while sensor1.color() != Color.WHITE:
        robo.drive(20, 60 * -lado)
    while sensor2.color() != Color.BLACK:
        robo.drive(20, 60 * lado)


while True:
    robo.drive(100, 0)
    while CorEsquerda.color() == Color.BLACK:
        robo.drive(20, -60)
        if CorDireita.color() == Color.BLACK:
            pretos(-1, CorEsquerda, CorDireita)

    while CorDireita.color() == Color.BLACK:
        robo.drive(20, 60)
        if CorEsquerda.color() == Color.BLACK:
            pretos(1, CorDireita, CorEsquerda)
