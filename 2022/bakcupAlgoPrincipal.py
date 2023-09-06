#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#inicando motores
motorEsquerdo = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE , gears=None)
motorDireito = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE , gears=None)
#inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito, wheel_diameter=39, axle_track=221)
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
    robo.turn(150)
    while sensorCorDireita.color() != Color.BLACK:
        robo.drive(0,25)
    while sensorCorDireita.color() != Color.WHITE:
        robo.drive(0,25)

def desviaObstaculo():
    ev3.speaker.beep()
    robo.straight(-60)
    robo.turn(55)
    robo.straight(60)
    while sensorCorDireita.color() !=Color.BLACK:
        robo.drive(50,-10)
    while sensorCorDireita.color() != Color.WHITE:
        robo.turn(5)
    ev3.speaker.beep()

    #ev3.speaker.beep() # <- Beep para indicar a inicialização de uma nova função 
    #robo.straight(-50) # Robô recua 10 cm 
    #robo.turn(90) # <- Robô vira 90°
    #robo.straight(130) # <- Robô avança 10 cm
    #robo.turn (-90)
    #robo.straight(300)
    #while sensorCorDireita.color() != Color.BLACK: # <-- Enquanto os sensores não identificarem preto, faça:
    #    robo.drive(80,-40) # <- Curva com velocidade de 200 e angulação 50°
    #robo.stop()
    #robo.turn(5)



#FUNÇÂO QUE ANDA PRA FRENTE NOS DOIS PRETOS
def doisPretos(testeDoisPretoCurva):
    robo.straight(25)
    #TESTA SE É 1
    if testeDoisPretoCurva == 1:#esquerda
        #robo.straight(20)
        robo.turn(35)
        robo.straight(50)
        #esquerdou
        testeDoisPretoCurva = None
        while sensorCorDireita.color() != Color.BLACK :
            robo.drive(0,-25)
    #TESTA SE É 2
    elif testeDoisPretoCurva == 2:#direita
        #robo.straight(20)
        robo.turn(-35)
        robo.straight(50)
        #Direitou
        testeDoisPretoCurva = None
        while sensorCorEsquerda.color() != Color.BLACK :
            robo.drive(0,25)

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
            robo.drive(-10,-30)
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
                robo.drive(50,0)
                
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
                    robo.drive(0,-25)
                while sensorCorEsquerda.color() != Color.WHITE:
                    robo.drive(0,-25)
                robo.straight(-20)
        elif travaEsquerda == True:
            while sensorCorEsquerda.color() != Color.GREEN:
                robo.drive(40,0)

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
            robo.drive(-10,30)
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
                robo.drive(50,0)
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
                    robo.drive(0,25)
                while sensorCorDireita.color() != Color.WHITE:
                    robo.drive(0,25)
                robo.straight(-20)
        elif travaDireita == True:
            while sensorCorDireita.color() != Color.GREEN:
                robo.drive(40,0)

#------------------------------------------------------------------------------

#WHILE PRINCIPAL
while True:
    x=0
    robo.drive(1024,0)
    if sensorCorDireita.color() == Color.YELLOW and sensorCorEsquerda.color() == Color.YELLOW:
        areaResgate()
    if sensorCorDireita.color() == Color.BLUE and sensorCorEsquerda.color() == Color.BLUE:
        areaResgate()

    if ultraSonico.distance() < 60: # ajeitar aq
        desviaObstaculo()

    if sensorCorDireita.color() == Color.GREEN and sensorCorEsquerda.color() == Color.GREEN:
        doisVerde()        

    if sensorCorEsquerda.color() != Color.WHITE:
        print('Esquerda')
        wait(50)
        robo.stop()
        wait(100)
        while x<=100:#<- adiciona valores numa lista para fazer a moda
            x += 1
            listaCorEsquerda.append(str(sensorCorEsquerda.color()))#<- adiciona as cores lidas na lista
        #print(listaCorEsquerda)
        wait(100)
        resultEsquerda = modaCor(listaCorEsquerda)#<- return do modaCor
        sensorEsquerdoTeste(resultEsquerda, travaVerde, testeDoisPretoCurva)
        listaCorEsquerda = []#<- reseta lista

    elif sensorCorEsquerda.color() == Color.WHITE:
        resultEsquerda = 2#<- declara que branco está endo lido
        sensorEsquerdoTeste(resultEsquerda, travaVerde, testeDoisPretoCurva)
        listaCorEsquerda = []#<- reseta lista



    if sensorCorDireita.color() != Color.WHITE:
        print('Direita')
        wait(50)
        robo.stop()
        wait(100)
        while x<=100:
            x += 1
            listaCorDireita.append(str(sensorCorDireita.color()))#<- adiciona as cores lidas na lista
        #print(listaCorDireita)
        wait(100)
        resultDireita = modaCor(listaCorDireita)#<- return do modaCor
        sensorDireitoTeste(resultDireita, travaVerde, testeDoisPretoCurva)
        listaCorDireita = []#<- reseta lista

    elif sensorCorDireita.color() == Color.WHITE:
        resultDireita = 2#<- 2 declara que branco está sendo lido
        sensorDireitoTeste(resultDireita, travaVerde, testeDoisPretoCurva)
        listaCorDireita = []#<- reseta lista