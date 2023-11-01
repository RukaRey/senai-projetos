class Veiculo:
    def __init__(self,marca,modelo):
        self.marca= marca
        self.modelo= modelo

    def ligar(self): 
        print(f"{self.modelo} está ligado.")

    def desligar(self):
        print(f"{self.modelo} está desligado.")

class Carro(Veiculo):
    def __init__(self,marca,modelo,numero_de_portas):
        super().__init__(marca,modelo)
        self.numero_de_portas= numero_de_portas
        self.portas= False

    def destravar_portas(self):
        self.portas= not self.portas
        if self.portas:
            print("Portas aberta.")
        else:
            print("Tudo fechado.")

class CarroEletrico(Carro):
    def __init__(self,marca,modelo,numero_de_portas):
        super().__init__(marca,modelo,numero_de_portas)
        self.batAtual=0

    def recarregarBateria(self):
        if self.batAtual==4:
            print("Carregado.")
        else:
            self.batAtual+=1
            print("Recarregando....")


class Moto(Veiculo):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.grau_state = False

    def grau(self):
        self.grau_state = not self.grau_state
        if self.grau_state:
            print("GRAU!!")
        else:
            print("Policia pintou....")

f= Carro("Fiat", "Uno",4)
m= Moto("Yamaha","Single")
me= CarroEletrico("Tesla","Elonquente",2)

me.ligar()
for i in range(0,5):
    me.recarregarBateria()

# f.ligar()
# f.desligar()

# f.destravar_portas()
# f.destravar_portas()

# m.ligar()
# m.desligar()

# m.grau()
# m.grau()