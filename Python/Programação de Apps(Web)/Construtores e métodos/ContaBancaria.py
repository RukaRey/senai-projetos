class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo

    def depositar(self,depo):
        self.saldo+=depo
        input(f"Saldo atual é de {self.saldo} reais.\nPressione Enter paa continuar....")

    def sacar(self,saq):
        if saq > self.saldo:
            input("Saque indisponível.\nPressione Enter paa continuar....")
        else:
            self.saldo-=saq
            input(f"Saldo atual é de {self.saldo} reais.\nPressione Enter paa continuar....")

# Usuários:
pessoa1=ContaBancaria("Jonas",3000)
pessoa2=ContaBancaria("Jenildo", 1800)

user=pessoa2 # Usuário atual(adaptável?)
while True:
    print(f"{user.titular}, saldo de {user.saldo}.")
    dess=input("O que fazer? \n(1)Depositar (2)Sacar")
    match dess:
        case '1':
            depo=int(input("Depositar quanto? "))
            user.depositar(depo)
        case '2':
            saq=int(input("Sacar quanto? "))
            user.sacar(saq)
