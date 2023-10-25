class Carro: # Criando a classe Carro()
    # Criando um método para exibir os atributos de um carro
    
    def exibirStats(self):
        carrao = self.marca,self.modelo,self.ano
        for atr in carrao:
            print(atr)
    def paraFrente(self):
        global destino
        if destino>4000:
            destino=4000
            pass
        else:
            destino -= self.vel
    def paraTrás(self):
        global destino
        if destino<0:
            destino=0
            pass
        else:
            destino += self.vel

destino = 4000


carro1 = Carro() # Criando uma instância da classe Carro()
carro1.marca = "VW"
carro1.modelo = "Gol"
carro1.ano = 2012
carro1.vel = 300

carro2 = Carro() # Criando outra instância da classe Carro()
carro2.marca = "Ford"
carro2.modelo = "Fiesta"
carro2.ano = 2016

carro3 = Carro() # Criando outra instância da classe Carro()
carro3.marca = "Chefrolet"
carro3.modelo = "Axis"
carro3.ano = 2050

carro4 = Carro() # Criando outra instância da classe Carro()
carro4.marca = "Uno"
carro4.modelo = "Guerra"
carro4.ano = 1866




while True:
    escolha=input("Oque fazer? ")
    match escolha:
        case '1':
            carro1.paraFrente()
            if destino<4000 and destino>0:
                print(f"Faltam {destino}Km para chegar em seu destino.")
            else:
                print("Você chegou ao seu destino.")
        case '2':
            carro1.paraTrás()
            if destino<0:
                print("Você chegou ao seu destino.")
            else:
                print(f"Faltam {destino}Km para chegar em seu destino.")
        case '3':
            carro1.exibirStats()



