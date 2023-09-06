#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
# Create your objects here.#inicando motores
motorEsquerdo = Motor(
    Port.A, positive_direction=Direction.CLOCKWISE, gears=None)
motorDireito = Motor(
    Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
# inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito,
                 wheel_diameter=37.3, axle_track=225)
# iniciando sensores de cor
CorEsquerda = ColorSensor(Port.S1)
CorDireita = ColorSensor(Port.S2)
cores = []
def detectaverde():
    corE = []
    corD = []
    for _ in range(80):
        robo.drive(30, 0)
        corE.append(CorEsquerda.color())
        corD.append(CorDireita.color())
        wait(1)
    for _ in range(100):
        robo.drive(30, 0)
        corE.append(CorEsquerda.color())
        corD.append(CorDireita.color())
        wait(1)

    pretoE = corE.count(Color.BLACK)
    verdeE = corE.count(Color.GREEN)
    brancoE = corE.count(Color.WHITE)

    pretoD = corD.count(Color.BLACK)
    verdeD = corD.count(Color.GREEN)
    brancoD = corD.count(Color.WHITE)
    if pretoE > verdeE and pretoE > brancoE:
        maiorE = Color.BLACK
    elif verdeE > pretoE and verdeE > brancoE:
        maiorE = Color.GREEN
    else:
        maiorE = Color.WHITE

    if pretoD > verdeD and pretoD > brancoD:
        maiorD = Color.BLACK
    elif verdeD > pretoD and verdeD > brancoD:
        maiorD = Color.GREEN
    else:
        maiorD = Color.WHITE

    return [maiorE, maiorD]


def verde90(lado, sensor1, sensor2):
    ev3.speaker.beep()
    while sensor1.color() != Color.WHITE and sensor1.color() != Color.WHITE:
        robo.drive(100, 0)
    robo.straight(10)
    while sensor1.color() != Color.BLACK:
        robo.drive(20, 60 * lado)
    robo.straight(20)


def pretos(lado, sensor1, sensor2):
    robo.straight(20)
    while sensor1.color() != Color.WHITE:
        robo.drive(20, 60 * -lado)
    while sensor2.color() != Color.BLACK:
        robo.drive(20, 60 * lado)

def passotras():
    for _ in range (100):
        robo.drive(-80,0)
        wait(1)
        if CorEsquerda.color() != Color.WHITE or CorDireita.color() != Color.WHITE:
            break
        
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
    if CorEsquerda.color() == Color.GREEN or CorDireita.color() == Color.GREEN:
        cores = detectaverde()
    if Color.GREEN in cores:
        ev3.speaker.beep()