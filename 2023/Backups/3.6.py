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
                 wheel_diameter=33.5, axle_track=208.5)
# iniciando sensores de cor
CorEsquerda = ColorSensor(Port.S1)
CorDireita = ColorSensor(Port.S4)
ultrassonico = UltrasonicSensor(Port.S3)

cores = []
nverdes = 0
apospreto = False


def detectaverde():
    corE = []
    corD = []
    for _ in range(80):
        robo.drive(20, 0)
        corE.append(CorEsquerda.color())
        corD.append(CorDireita.color())
        wait(1)
    for _ in range(100):
        robo.drive(-20, 0)
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


def doisverdes():
    robo.straight(-50)
    while CorDireita.color() != Color.BLACK:
        robo.drive(0, 60)
    robo.turn(20)


def verde90(lado, sensor1, sensor2):
    ev3.speaker.beep()
    while sensor1.color() != Color.WHITE:
        robo.drive(110, 30 * lado)
    while sensor1.color() != Color.BLACK:
        robo.drive(20, 60 * lado)
    while sensor2.color() == Color.BLACK:
        robo.drive(20, 60 * lado)
    while sensor2.color() != Color.BLACK:
        robo.drive(20, 60 * lado)


def doispretos(lado, sensor1, sensor2):
    for i in range(30):
        robo.drive(100, 0)
        wait(1)
    while sensor1.color() != Color.WHITE and sensor1.color() != Color.GREEN:
        robo.drive(20, 60 * -lado)
    while sensor2.color() != Color.BLACK:
        robo.drive(20, 60 * lado)



def obstaculo():
    lado = 1

    robo.stop()
    ev3.speaker.beep()

    wait(100)

    distancia = ultrassonico.distance() - 20
    robo.straight(distancia)
    robo.turn(90 * lado)
    robo.straight(180)
    robo.turn(90 * -lado)
    robo.straight(380)
    robo.turn(90 * - lado)
    robo.straight(80)
    while CorEsquerda.color() != Color.BLACK or CorDireita.color() != Color.BLACK:
        robo.drive(100, 0)
    robo.straight(40)
    robo.turn(90 * lado)


while True:
    robo.drive(100, 0)

    if ultrassonico.distance() < 40:
        obstaculo()

    while CorEsquerda.color() == Color.BLACK:
        robo.drive(20, -60)
        if CorDireita.color() == Color.BLACK:
            doispretos(-1, CorEsquerda, CorDireita)
            apospreto = True

    while CorDireita.color() == Color.BLACK:
        robo.drive(20, 60)
        if CorEsquerda.color() == Color.BLACK:
            doispretos(1, CorDireita, CorEsquerda)
            apospreto = True

    if CorEsquerda.color() == Color.WHITE and CorDireita.color() == Color.WHITE:
        apospreto = False

    if (CorEsquerda.color() == Color.GREEN or CorDireita.color() == Color.GREEN) and not apospreto:
        cores = detectaverde()
        nverdes = cores.count(Color.GREEN)

        if nverdes == 1:
            if cores[0] == Color.GREEN:
                verde90(-1, CorEsquerda, CorDireita)
            else:
                verde90(1, CorDireita, CorEsquerda)
        elif nverdes == 2:
            doisverdes()
        else:
            robo.straight(-50)

        cores = []
        nverdes = 0
