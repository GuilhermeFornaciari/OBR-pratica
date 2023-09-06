#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from resgate import *


#iniciando motores garra
motorGarra = Motor(Port.C)
motorCaixa = Motor(Port.D)
#inicando motores
motorEsquerdo = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE , gears=None)
motorDireito = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE , gears=None)
#inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito, wheel_diameter=41.4, axle_track=184.5)
#iniciando sensores de cor
sensorCorEsquerda = ColorSensor(Port.S1)
sensorCorDireita = ColorSensor(Port.S2)
#listas
listaCorEsquerda = []
listaCorDireita = []
#var
resultEsquerda = None
resultDireita = None
#ev3
ev3 = EV3Brick()
#trava verde
travaVerde = False #<- trava de curva verde
#sensor ultrasonico
ultraSonico = UltrasonicSensor(Port.S3)
#tste de curva no dois preto
testeDoisPretoCurva = None

wt = 5

while True:
    print('{}, {}'.format(sensorCorEsquerda.rgb(), sensorCorDireita.rgb()))