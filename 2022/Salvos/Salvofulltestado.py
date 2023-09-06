#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
#iniciando motores garra
motorGarra = Motor(Port.C)
motorCaixa = Motor(Port.D)
#inicando motores
motorEsquerdo = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE , gears=None)
motorDireito = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE , gears=None)
#inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito, wheel_diameter=40.7, axle_track=196)
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

#------------------------------------------------------------------------------

#MODA DA COR
def modaCor(lista):

#posições
#0 preto
#1 verde
#2 branco


    cont = [0,0,0] #<- contador

    for x in lista:# <- for que conta a quantidade de valor lido
        if x == 'Color.BLACK':
            cont[0] += 1
        elif x == 'Color.GREEN':
            cont[1] += 1
        elif x == 'Color.WHITE':
            cont[2] += 1

    maxValor = max(cont)# <- maior valor no cont
    index = cont.index(maxValor)# <- index

    print('0 = preto\n'+
    '1 = verde\n'+
    '2 = branco')

    print('index {} \n'.format(index))

    return index #<- retorna o index da cor


def doisVerde():
    ev3.speaker.beep()
    robo.turn(150)
    while sensorCorDireita.color() != Color.BLACK:
        robo.drive(0,80)
    while sensorCorDireita.color() != Color.WHITE:
        robo.drive(0,80)

#mudar
def desviaObstaculo():
    ev3.speaker.beep()
    ev3.speaker.beep()
    robo.stop()
    robo.straight(-20)
    robo.turn(-90)
    robo.straight(185)#165
    robo.turn(90)

    i=0
    while i!=25:
        robo.straight(10)
        if sensorCorDireita.color() == Color.BLACK:
            while sensorCorDireita.color() != Color.BLACK:
                robo.drive(80,40)
            robo.straight(30)
            while sensorCorDireita.color() != Color.BLACK:
                robo.drive(0,-100)
            break 
        i+=1

    while sensorCorDireita.color() != Color.BLACK:
        robo.drive(80,40)
    robo.straight(30)
    while sensorCorDireita.color() != Color.BLACK :
        robo.drive(0,-100)
    robo.turn(-15)


#FUNÇÂO QUE ANDA PRA FRENTE NOS DOIS PRETOS
def doisPretos(testeDoisPretoCurva):
    robo.straight(25)
    #TESTA SE É 1
    if testeDoisPretoCurva == 1:#esquerda
        #robo.straight(20)
        robo.turn(25)
        robo.straight(50)
        #esquerdou
        testeDoisPretoCurva = None
        while sensorCorDireita.color() != Color.BLACK :
            robo.drive(0,-80)
        robo.turn(10)
        robo.straight(15)
    #TESTA SE É 2
    elif testeDoisPretoCurva == 2:#direita
        #robo.straight(20)
        robo.turn(-25)
        robo.straight(50)
        #Direitou
        testeDoisPretoCurva = None
        while sensorCorEsquerda.color() != Color.BLACK :
            robo.drive(0,80)
        robo.turn(-10)
        robo.straight(15)
    

#------------------------------------------------------------------------------

#TESTE SENSOR ESQUERDO
def sensorEsquerdoTeste(alpha, travaVerde, testeDoisPretoCurva):
    verdes = False
    confirmaverde = True
    dopreto = False
    travaEsquerda = travaVerde

    if alpha == 2:#<- alpha == branco
        if travaEsquerda == True:
            ev3.speaker.beep()
            print('destravou')
            travaEsquerda = False

    if alpha == 0:#<- alpha == preto
        print('travou')
        travaEsquerda = True
        while sensorCorEsquerda.color() != Color.WHITE:
            testeDoisPretoCurva = 1
            robo.drive(-10,-80)
            #talvez seja necessario diminuir o -10
            if sensorCorDireita.color() != Color.WHITE:
                dopreto = True
                break
        robo.turn(-2)
        if sensorCorDireita.color() == Color.BLACK or dopreto:
            doisPretos(testeDoisPretoCurva)


    elif alpha == 1:#<- alpha == verde
        robo.straight(5)

        if travaEsquerda == False:

            robo.stop()

            while sensorCorEsquerda.color() != Color.WHITE:
                robo.drive(100,0)
                
                if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                    confirmaverde = False
                    verdes = False
                if sensorCorEsquerda.color() == Color.GREEN and sensorCorDireita.color() == Color.GREEN and confirmaverde:
                    robo.straight(5)
                    if sensorCorEsquerda.color() == Color.GREEN and sensorCorDireita.color() == Color.GREEN:
                        verdes = True
                        doisVerde()
                        break
            
            if verdes == False:
                robo.straight(15)
                while sensorCorEsquerda.color() != Color.BLACK:
                    robo.drive(0,-100)
                while sensorCorEsquerda.color() != Color.WHITE:
                    robo.drive(0,-100)
                
        elif travaEsquerda == True:
            while sensorCorEsquerda.color() != Color.GREEN:
                robo.drive(100,0)

#------------------------------------------------------------------------------

#TESTES SENSOR DIREITO
def sensorDireitoTeste(alpha, travaVerde, testeDoisPretoCurva):
    verdes = False
    confirmaverde = True
    dopreto = False
    travaDireita = travaVerde

    if alpha == 2:#<- alpha == branco
        if travaDireita == True:
            ev3.speaker.beep()
            print('destravou')
            travaDireita = False

    if alpha == 0:#<- alpha == preto
        print('travou')
        travaDireita = True
        while sensorCorDireita.color() != Color.WHITE:
            testeDoisPretoCurva = 2
            robo.drive(-10,80)
            #talvez seja necessario diminuir o -10
            if sensorCorEsquerda.color() != Color.WHITE:
                dopreto = True
                break               
        robo.turn(2) 
        if sensorCorEsquerda.color() == Color.BLACK or dopreto:
            doisPretos(testeDoisPretoCurva)

    elif alpha == 1:#<- alpha == verde
        robo.straight(5)

        if travaDireita == False:

            robo.stop()
            while sensorCorDireita.color() != Color.WHITE:
                robo.drive(120,0)

                if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                    confirmaverde = False
                    verdes = False
                if sensorCorEsquerda.color() == Color.GREEN and sensorCorDireita.color() == Color.GREEN and confirmaverde:
                    robo.straight(5)
                    if sensorCorEsquerda.color() == Color.GREEN and sensorCorDireita.color() == Color.GREEN:
                        verdes = True
                        doisVerde()
                        break
            
            if verdes == False:
                robo.straight(15)
                while sensorCorDireita.color() != Color.BLACK:
                    robo.drive(0,100)
                while sensorCorDireita.color() != Color.WHITE:
                    robo.drive(0,100)

        elif travaDireita == True:
            while sensorCorDireita.color() != Color.GREEN:
                robo.drive(100,0)

#------------------------------------------------------------------------------

#WHILE PRINCIPAL
while True:
    motorCaixa.hold()
    motorGarra.hold()

    x=0
    robo.drive(130,0)

    if sensorCorEsquerda.rgb() > (90,90,90) and sensorCorDireita.rgb() > (90,90,90):
        ev3.speaker.beep()

    if ultraSonico.distance() < 65: # ajeitar aq
        desviaObstaculo()

    if sensorCorDireita.color() == Color.GREEN and sensorCorEsquerda.color() == Color.GREEN:
        doisVerde()        

    if sensorCorEsquerda.color() != Color.WHITE:
        for x in range(70):
            robo.drive(-80,-25)
            wait(1)
        print('Esquerda')
        wait(wt)
        robo.drive(0,0)
        wait(wt)
        while x<=100:#<- adiciona valores numa lista para fazer a moda
            x += 1
            listaCorEsquerda.append(str(sensorCorEsquerda.color()))#<- adiciona as cores lidas na lista
        #print(listaCorEsquerda)

        resultEsquerda = modaCor(listaCorEsquerda)#<- return do modaCor
        sensorEsquerdoTeste(resultEsquerda, travaVerde, testeDoisPretoCurva)
        listaCorEsquerda = []#<- reseta lista

    elif sensorCorEsquerda.color() == Color.WHITE:
        resultEsquerda = 2#<- declara que branco está endo lido
        sensorEsquerdoTeste(resultEsquerda, travaVerde, testeDoisPretoCurva)
        listaCorEsquerda = []#<- reseta lista



    if sensorCorDireita.color() != Color.WHITE:
        for x in range(70):
            robo.drive(-80,25)
            wait(1)
        print('Direita')
        wait(wt)
        robo.drive(0,0)
        wait(wt)
        while x<=100:
            x += 1
            listaCorDireita.append(str(sensorCorDireita.color()))#<- adiciona as cores lidas na lista
        #print(listaCorDireita)
        resultDireita = modaCor(listaCorDireita)#<- return do modaCor
        sensorDireitoTeste(resultDireita, travaVerde, testeDoisPretoCurva)
        listaCorDireita = []#<- reseta lista

    elif sensorCorDireita.color() == Color.WHITE:
        resultDireita = 2#<- 2 declara que branco está sendo lido
        sensorDireitoTeste(resultDireita, travaVerde, testeDoisPretoCurva)
        listaCorDireita = []#<- reseta lista