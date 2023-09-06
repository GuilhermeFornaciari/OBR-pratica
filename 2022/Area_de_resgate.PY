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
garra = Motor(Port.D,positive_direction=Direction.COUNTERCLOCKWISE , gears=None)
caixa = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE , gears=None)
#inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito, wheel_diameter=39.7, axle_track=173.4)
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
#sensor ultrasonico e de toque
ultraSonico = UltrasonicSensor(Port.S3)
sensortoque = TouchSensor(Port.S4)
#tste de curva no dois preto
testeDoisPretoCurva = None

garra.reset_angle(0)
caixa.reset_angle(0)
garra.hold()


#------------------------------------------------------------------------------
#areaResgate()
tamanhorobo = 150 #largura
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
ev3.speaker.beep()
robo.stop()
robo.turn(90)
robo.straight(-40)# se ajustar na parede
wait(100)
if ultraSonico.distance() > 100:#entrada na esquerda
    robo.turn(-90) #robo gira 90 pra esquerda e volta pra posição inicial
    garra.run_until_stalled(-200, Stop.HOLD, 50) # abaixar a garra
    while True: #função da varredura
        n = 0
        while sensortoque.pressed() == False:#robo anda pra frente até o sensor de toque ser pressionado
            robo.drive(120,0)
            if sensorCorEsquerda.Color() == color.BLACK or sensorCorDireita.Color() == color.BLACK:
                if sensorCorEsquerda.Color() == color.BLACK:
                    while sensorCorEsquerda.Color() == color.BLACK:
                        robo.drive(0,30)
                    robo.straight(180)
                    robo.turn(45)
                    n = 1
                
            if sensorCorDireita.Color() == color.GREEN or sensorCorEsquerda.Color() == color.GREEN:
                if sensorCorDireita.Color() == color.GREEN and sensorCorEsquerda.Color() != color.GREEN:
                    while sensorCorEsquerda.Color() != color.GREEN:
                        robo.drive(0, 10)
                if sensorCorDireita.Color() == color.GREEN and sensorCorEsquerda.Color() != color.GREEN:
                    while sensorCorEsquerda.Color() != color.GREEN:
                        robo.drive(0, -10)
                robo.turn(90)
                n = 1
                break
        robo.stop()
        if n = 0:
            robo.straight(-25) #anda um pouco pra trás 
            garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
            robo.straight(-90) #robo vai para trás
            garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
            garra.reset_angle(0)
            wait(100)
            robo.straight(120)
            robo.stop()
            robo.turn(90)#robo vira para a direita
            wait(100)
        garra.run_until_stalled(-50, Stop.HOLD, 50) # abaixa a garra
        wait(100)
        #if ultraSonico.distance() <= 100 or sensortoque.pressed() == True: #se o sensor de toque for pressionado ou a distancia for menor que 10 cm
            #if sensortoque.pressed() == False: #se o sensor não foi pressionado, robo anda um pouco
                #robo.straight(60)
            #wait(1000)
            #if ultraSonico.distance() >= 100: # se a distancia for maior que 100, seria a área de resgate
                #robo.turn(90) #robo gira 90 - e continua
            #else: # se não for maior é que está na parede e acabou a varredura
                #robo.turn(90)#se alinha a parede
                #ev3.speaker.beep()
                #break 
        #else: # se o sensor de toque não for pressionado ou a distancia não for menor ou igual a 100
            #ev3.speaker.beep()
            #robo.straight(tamanhorobo) #robo anda sua largura
            #robo.turn(90) #gira 90
        #while (sensortoque.pressed() == False) or (ultraSonico.distance() > 50): #enquanto o sensor não for pressionado
            #ev3.speaker.beep()
            #robo.drive(120,0)
        #robo.stop()
        #robo.straight(-30) #faz o movimento da garra
        #garra.run_angle(30,40,Stop.HOLD, wait=True) # garra ergue
        #print('ok')
        #robo.straight(-90) #robo vai para trás
        #garra.run_until_stalled(10000, Stop.HOLD, 100) # garra ergue (posição inicial)
        #garra.reset_angle(0)
        #wait(100)
        #robo.straight(130)
        #robo.stop()
        #robo.turn(-104.6) #robo gira pra esquerda 90
        #wait(1000)
        #garra.run_until_stalled(-50, Stop.HOLD, 50) # garra abaixa
        #wait(1000)
        #if ultraSonico.distance() < 100 or sensortoque.pressed() == True: # mesmo esquema de conferência porém para esquerda
            #if sensortoque.pressed() == False:
                #robo.straight(70)
            #wait(1000)
            #i#f ultraSonico.distance() > 100:
                #robo.turn(-52.3)
            #else: 
                #robo.turn(-209.2) #gira 180 e começa a procurar a area de resgate
                #ev3.speaker.beep()
                #break 
        #else: 
            #robo.straight(tamanhorobo)
            #robo.turn(-104.6)

    #while True:#buscando área de resgate para pôr as bolinhas
        #robo.drive(100,0)
        #if sensorCorEsquerda.Color() == color.RED or sensorCorEsquerda.Color() == color.RED:
            #robo.turn(90)
        #if sensortoque.preset() == True:
            #if ultraSonico.distance() > 90:
                #robo.straight(-20)
                #robo.turn(45)
                #robo.straight(90)
                #robo.turn(90)
                #robo.straight(-100)
                #garra.run_until_stalled(-50, Stop.HOLD, 50) # garra abaixa
                #caixa.run_until_stalled(200, Stop.HOLD, 100) # abaixa a caixa
        #falta terminar