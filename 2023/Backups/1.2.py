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

    for i in range(50):
        robo.drive(100, 0)
        wait(1)
    while sensor.color() != Color.BLACK:
        robo.drive(50, 50 * -lado)


while True:
    robo.drive(100, 0)
    while CorEsquerda.color() == Color.BLACK:
        for i in range(10):
            robo.drive(20, -60)
            wait(1)
            if CorDireita.color() == Color.BLACK:
                pretos(-1, CorEsquerda)

    while CorDireita.color() == Color.BLACK:
        for x in range(10):
            robo.drive(20, 60)
            wait(1)
        if CorEsquerda.color() == Color.BLACK:
            pretos(1, CorDireita)


# Write your program here.
ev3.speaker.beep()
