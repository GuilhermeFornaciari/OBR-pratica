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
#sensor ultrasonico e de toque
ultraSonico = UltrasonicSensor(Port.S3)
sensortoque = TouchSensor(Port.S4)
#tste de curva no dois preto
testeDoisPretoCurva = None

garra.reset_angle(0)
caixa.reset_angle(0)
garra.hold()

#  1.0 <- inicio do algoritimo ->
def execut():
    # função de saida da área de resgate
    def saida():
        if saidaPossivel  == 'direitaBAIXO':
            valorFrentePercurso = ultraSonico.distance()
            robo.straight(valorFrentePercurso/2)
            robo.turn(-90)
            valorFrentePercurso = ultraSonico.distance()
            robo.straight(valorFrentePercurso/2)
            
            #igual para todos
            while True:
                robo.turn(10)
                if ultraSonico.distance() > 800:
                    robo.drive(100,0)
                    if sensorCorEsquerda.color() == Color.GREEN or sensorCorDireita.color() == Color.GREEN:
                        robo.straight(tamanhoRobo)
                        while True:
                            robo.turn((10+achaLinhaSoma))
                            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                                #retorna para segue linha
                                print('seguelinha')
                                break
                            y = (achaLinhaSoma * -1) # <- transform numeor positivo em negativo
                            robo.turn((-10-y))
                            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                                #retorna para segue linha
                                print('seguelinha')
                                break
                            else: 
                                if achaLinhaSoma > 100 :
                                    break
                                achaLinhaSoma += 10
                    else: 
                        robo.drive(ultraSonico.distance()/2)
        elif  saidaPossivel  == 'esquerdaBAIXO':            
            
            valorFrentePercurso = ultraSonico.distance()
            robo.straight(valorFrentePercurso/2)
            robo.turn(-90)
            valorFrentePercurso = ultraSonico.distance()
            robo.straight(valorFrentePercurso/2)
        
            #igual para todos
            while True:
                robo.turn(10)
                if ultraSonico.distance() > 800:
                    robo.drive(100,0)
                    if sensorCorEsquerda.color() == Color.GREEN or sensorCorDireita.color() == Color.GREEN:
                        robo.straight(tamanhoRobo)
                        while True:
                            robo.turn((10+achaLinhaSoma))
                            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                                #retorna para segue linha
                                print('seguelinha')
                                break
                            y = (achaLinhaSoma * -1) # <- transform numeor positivo em negativo
                            robo.turn((-10-y))
                            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                                #retorna para segue linha
                                print('seguelinha')
                                break
                            else: 
                                if achaLinhaSoma > 100 :
                                    break
                                achaLinhaSoma += 10
                    else: 
                        robo.drive(ultraSonico.distance()/2)       
        elif  saidaPossivel  == 'direitaCIMA':

            valorFrentePercurso = ultraSonico.distance()
            robo.straight(valorFrentePercurso/2)
            robo.turn(90)
            valorFrentePercurso = ultraSonico.distance()
            robo.straight(valorFrentePercurso/2)
            
            #igual para todos
            while True:
                robo.turn(10)
                if ultraSonico.distance() > 800:
                    robo.drive(100,0)
                    if sensorCorEsquerda.color() == Color.GREEN or sensorCorDireita.color() == Color.GREEN:
                        robo.straight(tamanhoRobo)
                        while True:
                            robo.turn((10+achaLinhaSoma))
                            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                                #retorna para segue linha
                                print('seguelinha')
                                break
                            y = (achaLinhaSoma * -1) # <- transform numeor positivo em negativo
                            robo.turn((-10-y))
                            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                                #retorna para segue linha
                                print('seguelinha')
                                break
                            else: 
                                if achaLinhaSoma > 100 :
                                    break
                                achaLinhaSoma += 10
                    else: 
                        robo.drive(ultraSonico.distance()/2)
        elif   saidaPossivel  == 'esquerdaCIMA':
            
            robo.turn(-90)
            valorFrentePercurso = ultraSonico.distance()
            robo.straight(valorFrentePercurso/2)
            robo.turn(90)
            valorFrentePercurso = ultraSonico.distance()
            robo.straight(valorFrentePercurso/2)
            
            #igual para todos
            while True:
                robo.turn(10)
                if ultraSonico.distance() > 800:
                    robo.drive(100,0)
                    if sensorCorEsquerda.color() == Color.GREEN or sensorCorDireita.color() == Color.GREEN:
                        robo.straight(tamanhoRobo)
                        while True:
                            robo.turn((10+achaLinhaSoma))
                            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                                #retorna para segue linha
                                print('seguelinha')
                                break
                            y = (achaLinhaSoma * -1) # <- transform numeor positivo em negativo
                            robo.turn((-10-y))
                            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                                #retorna para segue linha
                                print('seguelinha')
                                break
                            else: 
                                if achaLinhaSoma > 100 :
                                    break
                                achaLinhaSoma += 10
                    else: 
                        robo.drive(ultraSonico.distance()/2)
    # função de soltar as bolinhas na área de resgate
    def soltarBolinhas():
        print('Soltar as bolinhas área de resgate')
        #algoritimo
        saida()
        
    # 1.1 <- variavéis ->
    y=0
    achaLinhaSoma = 0
    retentativaBotao = 100
    tamanhoRobo = 170 # comprimento do robo
    valorFrente = 0 # valor lido na frente logo na entrada
    valorFrentePercurso = 0 # valor lido na frente durante o percurso
    valorLado = 0 # valor lido no lado logo na entrada
    ladoEntrada = None # 1:esquerda   | 2:direita
    saidaPossivel = '' # local onde tem uma possivél saída
    valorAndarLado = 0 # valor que falta para andar ao lado
    # <------------->

    robo.straight((tamanhoRobo + 10))

    # 1.2 <- leitura de dados ->
    robo.stop()

    # lê a distancia da entrada da parede da frente
    valorFrente = ultraSonico.distance() 

    # virar para direita e ajusta na parede
    robo.turn(90) 
    robo.straight(-50)

    # lê a distancia da entrada da parede ao lado
    valorLado = ultraSonico.distance() 
    valorAndarLado = valorLado

    # PS: medidas de leitura em média 720 para parede distante

    # posiciona o robinho no ponto inicial
    robo.straight(50)
    robo.turn(-90)
    # <-------------------->

    # 1.3 <- verifica lado de entrada ->
    if valorLado > 200: # lado de entrada esquerda
        ladoEntrada = 1
    elif valorLado < 200: # lado de entrada direito
        ladoEntrada = 2
    # <---------------------------->


    # 1.4 <- algoritimo ->
    #OBS: ladoEntrada==1 (entrada na esquerda)
    #     ladoEntrada==2 (entrada na direita)


    if ladoEntrada == 1:
        
        robo.turn(-90)
        
        # se a saída for logo em frente a entrafa realiza está função
        if valorFrente > 800:
            robo.turn(90)
            robo.straight(tamanhoRobo)
            robo.turn(-90)
            
        # ! 1º varredura !
        # alinhamento para ir rente á parede
        while ultraSonico.distance() < 670:
            robo.drive(0,-25) # Virar para esquerda
            
        # abaixa a garra    
        garra.run_until_stalled(-200, Stop.HOLD, 50) # abaixar a garra
        robo.straight
        #até que o botão seja pressionado ele seguira em frente
        while sensortoque.pressed() != True: #
            robo.drive(100,0)
        
        limitador = 0# <- variavél limitador
        while True:
            if sensortoque.pressed() == True:
                robo.straight(-25) #anda um pouco pra trás 
                garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                robo.straight(-90) #robo vai para trás
                garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                garra.reset_angle(0)
                robo.straight(90)# <- anda para frente após levantar garra
                break
            else: 
                if limitador == 2:
                    break
                robo.straight(-30)
                robo.straight(retentativaBotao)# se andar de mais para frente diminuir
                limitador += 1
                
        # ! 1º curva !
        robo.turn(90)
        valorFrentePercurso = ultraSonico.distance() 
        
        if valorFrentePercurso < (tamanhoRobo/2)+30:
            robo.turn(90) # se a parede estiver próxima ele vira para baixo
        else: 
            robo.straight(tamanhoRobo) # anda tamanho do robo
            robo.turn(90) # vira para baixo
            valorFrentePercurso = ultraSonico.distance()# recebe o tamanho do percurso
        # !!
        # !!
        # ! 2º varedura !
        
        #baixa a garra
        garra.run_until_stalled(-50, Stop.HOLD, 50)
        
        # se ele ainda estiver detectando entrada ainda o tamanho que leu quando entrou na pista menos 
        # o seu tamanho, se a possivel saida estiver na frente, usa o dado lateral
        if valorFrentePercurso > 800:
            if saidaPossivel != 'frente':
                robo.straight((valorFrente-tamanhoRobo))
            else:
                robo.straight((valorLado-tamanhoRobo))
        else:
            robo.straight(valorFrentePercurso) # anda o tamanho do percurso
            
        # levantar garra
        while True:
            if sensortoque.pressed() == True:
                robo.straight(-25) #anda um pouco pra trás 
                garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                robo.straight(-90) #robo vai para trás
                garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                garra.reset_angle(0)
                break
            else: 
                if limitador == 2:
                    robo.straight(-25) #anda um pouco pra trás 
                    garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                    robo.straight(-90) #robo vai para trás
                    garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                    garra.reset_angle(0)
                    robo.straight(90)# <- anda para frente após levantar garra
                    break
                robo.straight(-30)
                robo.straight(retentativaBotao)# se andar de mais para frente diminuir
                limitador += 1
        
        # ! 2º curva !
        robo.turn(-90)
        valorFrentePercurso = ultraSonico.distance() 
        
        if valorFrentePercurso < (tamanhoRobo/2)+30:
            robo.turn(-90) # se a parede estiver próxima ele vira para baixo
        else: 
            robo.straight(tamanhoRobo) # anda tamanho do robo
            robo.turn(-90) # vira para baixo
            valorFrentePercurso = ultraSonico.distance()# recebe o tamanho do percurso
        
        #POSSIVÉL BUG AQUI    
        #possivél sáida a frente
        while True:
            if valorFrentePercurso > 800:
                robo.turn(90)
                robo.straight(tamanhoRobo)
                robo.turn(-90)
                valorFrentePercurso = ultraSonico.distance()# recebe o tamanho do percurso
                if valorFrentePercurso > 800:
                    robo.turn(90)
                    robo.straight(tamanhoRobo)
                    robo.turn(-90)
                    break
                else:
                    break
            # possivél correção do BUG
            else:
                break
            
        # abaixa a garra
        garra.run_until_stalled(-50, Stop.HOLD, 50) # abaixa a garra
        
        #
        # !3º varedura!
        while sensortoque.pressed() != True: 
            robo.drive(100,0)
            
        limitador = 0 #variavél limitadora
        while True:
            if sensortoque.pressed() == True:
                robo.straight(-25) #anda um pouco pra trás 
                garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                robo.straight(-90) #robo vai para trás
                garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                garra.reset_angle(0)
                robo.straight(90)
                break
            else: 
                if limitador == 2:
                    break
                robo.straight(-30)
                robo.straight(retentativaBotao)# se andar de mais para frente diminuir
                limitador += 1
                
        # ! 3º curva !
        robo.turn(90)
        valorFrentePercurso = ultraSonico.distance() 
        
        if valorFrentePercurso < (tamanhoRobo/2)+30:
            robo.turn(90) # se a parede estiver próxima ele vira para baixo
        else: 
            robo.straight(tamanhoRobo) # anda tamanho do robo
            robo.turn(90) # vira para baixo
            valorFrentePercurso = ultraSonico.distance()# recebe o tamanho do percurso
            
        # ! varedura final !
        # abaixa a garra
        garra.run_until_stalled(-50, Stop.HOLD, 50) # abaixa a garra
        
        # !4º varedura!
        while sensortoque.pressed() != True: 
            robo.drive(100,0)
            
        limitador = 0 #variavél limitadora
        while True:
            if sensortoque.pressed() == True:
                robo.straight(-25) #anda um pouco pra trás 
                garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                robo.straight(-90) #robo vai para trás
                garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                garra.reset_angle(0)
                robo.straight(90)
                break
            else: 
                if limitador == 2:
                    break
                robo.straight(-30)
                robo.straight(retentativaBotao)# se andar de mais para frente diminuir
                limitador += 1
                
        if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
            #direita em baixo
            saidaPossivel = 'direitaBAIXO'
            robo.turn(180)
            soltarBolinhas()
        elif sensorCorEsquerda.color() != Color.BLACK or sensorCorDireita.color() != Color.BLACK:
            robo.turn(180)# meia volta
            while (sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK) or ultraSonico.distance() < (tamanhoRobo/2):
                robo.drive(100,0)
            #direita em cima
            saidaPossivel = 'direitaCIMA'
            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                robo.turn(-180)
                soltarBolinhas()
            elif sensorCorEsquerda.color() != Color.BLACK or sensorCorDireita.color() != Color.BLACK: 
                robo.turn(-90)
                while (sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK) or ultraSonico.distance() < (tamanhoRobo/2):
                    robo.drive(100,0)
                saidaPossivel = 'esquerdaCIMA'
                #esquerda em cima
                if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                    robo.turn(-180)
                    soltarBolinhas()
                
    if ladoEntrada == 2:
        
        robo.turn(90)
        
        # se a saída for logo em frente a entrafa realiza está função
        if valorFrente > 800:
            robo.turn(-90)
            robo.straight(tamanhoRobo)
            robo.turn(90)
            
        # ! 1º varredura !
        # alinhamento para ir rente á parede
        while ultraSonico.distance() < 670:
            robo.drive(0,25) # Virar para direita
            
        # abaixa a garra    
        garra.run_until_stalled(-200, Stop.HOLD, 50) # abaixar a garra
        robo.straight
        #até que o botão seja pressionado ele seguira em frente
        while sensortoque.pressed() != True: #
            robo.drive(100,0)
        
        limitador = 0# <- variavél limitador
        while True:
            if sensortoque.pressed() == True:
                robo.straight(-25) #anda um pouco pra trás 
                garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                robo.straight(-90) #robo vai para trás
                garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                garra.reset_angle(0)
                robo.straight(90)# <- anda para frente após levantar garra
                break
            else: 
                if limitador == 2:
                    break
                robo.straight(-30)
                robo.straight(retentativaBotao)# se andar de mais para frente diminuir
                limitador += 1
                
        # ! 1º curva !
        robo.turn(-90)
        valorFrentePercurso = ultraSonico.distance() 
        
        if valorFrentePercurso < (tamanhoRobo/2)+30:
            robo.turn(-90) # se a parede estiver próxima ele vira para baixo
        else: 
            robo.straight(tamanhoRobo) # anda tamanho do robo
            robo.turn(-90) # vira para baixo
            valorFrentePercurso = ultraSonico.distance()# recebe o tamanho do percurso
        # !!
        # !!
        # ! 2º varedura !
        
        #baixa a garra
        garra.run_until_stalled(-50, Stop.HOLD, 50)
        
        # se ele ainda estiver detectando entrada ainda o tamanho que leu quando entrou na pista menos 
        # o seu tamanho, se a possivel saida estiver na frente, usa o dado lateral
        if valorFrentePercurso > 800:
            if saidaPossivel != 'frente':
                robo.straight((valorFrente-tamanhoRobo))
            else:
                robo.straight((valorLado-tamanhoRobo))
        else:
            robo.straight(valorFrentePercurso) # anda o tamanho do percurso
            
        # levantar garra
        while True:
            if sensortoque.pressed() == True:
                robo.straight(-25) #anda um pouco pra trás 
                garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                robo.straight(-90) #robo vai para trás
                garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                garra.reset_angle(0)
                break
            else: 
                if limitador == 2:
                    robo.straight(-25) #anda um pouco pra trás 
                    garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                    robo.straight(-90) #robo vai para trás
                    garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                    garra.reset_angle(0)
                    robo.straight(90)# <- anda para frente após levantar garra
                    break
                robo.straight(-30)
                robo.straight(retentativaBotao)# se andar de mais para frente diminuir
                limitador += 1
        
        # ! 2º curva !
        robo.turn(90)
        valorFrentePercurso = ultraSonico.distance() 
        
        if valorFrentePercurso < (tamanhoRobo/2)+30:
            robo.turn(90) # se a parede estiver próxima ele vira para baixo
        else: 
            robo.straight(tamanhoRobo) # anda tamanho do robo
            robo.turn(90) # vira para baixo
            valorFrentePercurso = ultraSonico.distance()# recebe o tamanho do percurso
        
        #POSSIVÉL BUG AQUI    
        #possivél sáida a frente
        while True:
            if valorFrentePercurso > 800:
                robo.turn(-90)
                robo.straight(tamanhoRobo)
                robo.turn(90)
                valorFrentePercurso = ultraSonico.distance()# recebe o tamanho do percurso
                if valorFrentePercurso > 800:
                    robo.turn(-90)
                    robo.straight(tamanhoRobo)
                    robo.turn(90)
                    break
                else:
                    break
            # possivél correção do BUG
            else:
                break
            
        # abaixa a garra
        garra.run_until_stalled(-50, Stop.HOLD, 50) # abaixa a garra
        
        #
        # !3º varedura!
        while sensortoque.pressed() != True: 
            robo.drive(100,0)
            
        limitador = 0 #variavél limitadora
        while True:
            if sensortoque.pressed() == True:
                robo.straight(-25) #anda um pouco pra trás 
                garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                robo.straight(-90) #robo vai para trás
                garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                garra.reset_angle(0)
                robo.straight(90)
                break
            else: 
                if limitador == 2:
                    break
                robo.straight(-30)
                robo.straight(retentativaBotao)# se andar de mais para frente diminuir
                limitador += 1
                
        # ! 3º curva !
        robo.turn(-90)
        valorFrentePercurso = ultraSonico.distance() 
        
        if valorFrentePercurso < (tamanhoRobo/2)+30:
            robo.turn(-90) # se a parede estiver próxima ele vira para baixo
        else: 
            robo.straight(tamanhoRobo) # anda tamanho do robo
            robo.turn(-90) # vira para baixo
            valorFrentePercurso = ultraSonico.distance()# recebe o tamanho do percurso
            
        # ! varedura final !
        # abaixa a garra
        garra.run_until_stalled(-50, Stop.HOLD, 50) # abaixa a garra
        
        # !4º varedura!
        while sensortoque.pressed() != True: 
            robo.drive(100,0)
            
        limitador = 0 #variavél limitadora
        while True:
            if sensortoque.pressed() == True:
                robo.straight(-25) #anda um pouco pra trás 
                garra.run_angle(30,40,Stop.HOLD, wait=True) #ergue um pouco a garra
                robo.straight(-90) #robo vai para trás
                garra.run_until_stalled(10000, Stop.HOLD, 100) # ergue tudo a garra (posição inicial)
                garra.reset_angle(0)
                robo.straight(90)
                break
            else: 
                if limitador == 2:
                    break
                robo.straight(-30)
                robo.straight(retentativaBotao)# se andar de mais para frente diminuir
                limitador += 1
                
        if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
            #direita em baixo
            saidaPossivel = 'direitaCIMA'
            robo.turn(180)
            soltarBolinhas()
        elif sensorCorEsquerda.color() != Color.BLACK or sensorCorDireita.color() != Color.BLACK:
            robo.turn(180)# meia volta
            while (sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK) or ultraSonico.distance() < (tamanhoRobo/2):
                robo.drive(100,0)
            #direita em cima
            saidaPossivel = 'esquerdaBAIXO'
            if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                robo.turn(-180)
                soltarBolinhas()
            elif sensorCorEsquerda.color() != Color.BLACK or sensorCorDireita.color() != Color.BLACK: 
                robo.turn(-90)
                while (sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK) or ultraSonico.distance() < (tamanhoRobo/2):
                    robo.drive(100,0)
                saidaPossivel = 'esquerdaCIMA'
                #esquerda em cima
                if sensorCorEsquerda.color() == Color.BLACK or sensorCorDireita.color() == Color.BLACK:
                    robo.turn(-180)
                    soltarBolinhas()
    # <-------------->