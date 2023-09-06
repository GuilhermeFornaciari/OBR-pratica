#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import threading

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


def pretos(lado, sensor):

    robo.turn(5*-lado)
    if sensor.color() == Color.BLACK:
        robo.straight(50)
        if lado == -1:  # Esquerda
            for i in range(450):
                robo.drive(5, 60)
                if CorDireita.color() == Color.BLACK:
                    robo.turn(10)
                    break

            while CorEsquerda.color() != Color.BLACK and CorDireita.color() != Color.BLACK:
                robo.drive(-5, -60)
        else:  # Direita
            for i in range(450):
                robo.drive(5, -60)
                if CorEsquerda.color() == Color.BLACK:
                    robo.turn(-10)
                    break
            while CorEsquerda.color() != Color.BLACK and CorDireita.color() != Color.BLACK:
                robo.drive(-5, 60)


while True:
    robo.drive(100, 0)
    while CorEsquerda.color() == Color.BLACK:
        robo.drive(20, -60)
        if CorDireita.color() == Color.BLACK:
            pretos(-1, CorEsquerda)

    while CorDireita.color() == Color.BLACK:
        robo.drive(20, 60)
        if CorEsquerda.color() == Color.BLACK:
            pretos(1, CorDireita)


# Write your program here.
ev3.speaker.beep()
