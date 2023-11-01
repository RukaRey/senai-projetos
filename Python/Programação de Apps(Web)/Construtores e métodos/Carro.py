class Carro:
    def __init__(self,marca,modelo,tanque_de_combustivel,consumo):
        self.marca=marca
        self.modelo=modelo
        self.tanque_de_combustivel=tanque_de_combustivel
        self.consumo=consumo

    def dirigir(self,distancia):
        if self.tanque_de_combustivel<=0:
            input("Sem gasolina.")
        else:
            self.tanque_de_combustivel-=distancia*self.consumo

    def abastecer(self,litros):
        if litros>self.tanque_de_combustivel:
            input("Capacidade do tanque excedida.")
        else:
            self.tanque_de_combustivel+= litros

carro1=Carro("Fiat","Uno",100,2)
carro2=Carro("Tesla","NewAge",80,5)

carroAt=carro1
while True:
    print(f"Meu carro tem {carroAt.tanque_de_combustivel}L de capacidade do tanque e consome {carroAt.consumo} por Km.")
    dess=input("O que fazer? \n(1)Dirigir (2)Abastecer")
    match dess:
        case '1':
            km=int(input("Quantos km?"))
            carroAt.dirigir(km)
        case '2':
            gas=int(input("Quantos litros? "))
            carroAt.abastecer(gas)