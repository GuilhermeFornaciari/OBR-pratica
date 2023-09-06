class Coordenadas:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def Area_Resgate():
    FazCurva = 15
    voltar = -80
    Travakit = 0
    coordenadas_resgate_vivas = Coordenadas()
    coordenadas_resgate_mortas = Coordenadas()

    def corbola():
        listaCorBola = []
        for _ in range(100):
            wait(3)
            robo.drive(0, 20)
            robo.drive(20, 0)
            listaCorBola.append(CorFrente.color())
        return listaCorBola

    def Parado():
        ListaLida = []
        for _ in range(100):
            wait(3)
            ListaLida.append(CorFrente.color())
        return ListaLida

    def DeixaKit():
        robo.straight(voltar)
        robo.turn(180)
        robo.straight(voltar)
        motorGarra.run_target(100, Abrida, then=Stop.HOLD, wait=True)
        motorGarra.run_target(100, PosicaoFechada, then=Stop.HOLD, wait=True)
        Travakit += 1

    def PegaBola():
        robo.straight(voltar)
        robo.turn(180)
        motorGarra.run_target(100, Abrida, then=Stop.HOLD, wait=True)
        robo.straight(voltar)
        motorGarra.run_target(100, PosicaoFechada, then=Stop.HOLD, wait=True)

    def Volta_Para_Coordenada(coordenada):
        distancia_x = robo.x - coordenada.x
        distancia_y = robo.y - coordenada.y

        robo.turn(180)
        robo.turn(-90) if distancia_x > 0 else robo.turn(90)
        robo.straight(distancia_x)

        robo.turn(180)
        robo.straight(abs(distancia_y))

while True:
    FazCurva += 15
    if FazCurva > 180:
        FazCurva = 0
        FazCurva += -15
        
    if ultrassonico.distance() < 20:
        listaCoresParado = Parado()
        cor_mais_frequente_parado = max(set(listaCoresParado), key=listaCoresParado.count)
        
        listaCoresBolinha = corbola()
        cor_mais_frequente_bolinha = max(set(listaCoresBolinha), key=listaCoresBolinha.count)
        
        robo.drive(FazCurva, 0)
        
            if cor_mais_frequente_parado == Color.WHITE:
                robo.straight(voltar)
                robo.turn(FazCurva)
            elif cor_mais_frequente_parado == Color.GREEN:
                coordenadas_resgate_vivas = Coordenadas(robo.x, robo.y)
                if Travakit == 0:
                    DeixaKit()
            elif cor_mais_frequente_parado == Color.RED:
                coordenadas_resgate_mortas = Coordenadas(robo.x, robo.y)
                if Travakit == 0:
                    DeixaKit()

            elif cor_mais_frequente_bolinha == Color.BLACK:
                PegaBola()
                coordenadas_resgate_mortas = Coordenadas(robo.x, robo.y)
                Volta_Para_Coordenada(coordenadas_resgate_mortas)
                
            elif cor_mais_frequente_bolinha != Color.WHITE and cor_mais_frequente_bolinha != Color.WHITE and cor_mais_frequente_bolinha != Color.GREEN and cor_mais_frequente_bolinha != Color.RED and cor_mais_frequente_bolinha != Color.BLACK:
                PegaBola()
                coordenadas_resgate_vivas = Coordenadas(robo.x, robo.y)
                Volta_Para_Coordenada(coordenadas_resgate_vivas)
                wait(5)   