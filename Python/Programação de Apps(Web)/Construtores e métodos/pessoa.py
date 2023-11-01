class Pessoa:
    # Atributos:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    # Métodos
    def talk(self):
        print(f"{self.name} is talking....")
    def bday(self):
        print(self.age)
        self.age+=1
        

mero=Pessoa("Juan",18,1.90)
pessoa2=Pessoa("Luciano",12,1.75)

mero.talk()
pessoa2.talk()

while True:
    mero.bday()
    pessoa2.bday()
    input("Insert any key to continue....")

