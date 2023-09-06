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
                 wheel_diameter=37.1, axle_track=234)
# iniciando sensores de cor
CorEsquerda = ColorSensor(Port.S4)
CorDireita = ColorSensor(Port.S1)
ultrassonico = UltrasonicSensor(Port.S3)
cor =  CorDireita.reflection()
cor1 = CorEsquerda.reflection()
print("Direita = "+cor + "  Esquerda = " + cor1)