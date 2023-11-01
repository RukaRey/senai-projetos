class Banco:
    def __init__(self):
        self.saldo = 0
    def __str__(self):
        return f"Saldo do Banco: {self.saldo}"
class Cliente:
    def __init__(self,saldo,valor):
        self.saldo=saldo
        self.valor=valor
class Ouro(Cliente):
    def __init__(self,saldo,valor):
        super().__init__(saldo,valor)
        self.tarifa=15+valor*0.02
class Prata(Cliente):
    def __init__(self,saldo,valor):
        super().__init__(saldo,valor)
        self.tarifa=15+valor*0.05
class Bronze(Cliente):
    def __init__(self,saldo,valor):
        super().__init__(saldo,valor)
        self.tarifa=15+valor*0.10

# Clientes
mario=Ouro(9999,99)
luigi=Prata(2220,200)
toad=Bronze(200,5)
# Banco
BancoUniãoFinanceira=Banco()
BancoCentraldoCerrado=Banco()
BancodaSerraDourada=Banco()

def mostrar_saldo(cliente):
    print(f"Saldo do cliente: {cliente.saldo}")

def realizar_transferencia(origem,destino,valor):
    destino.saldo+=valor
    origem.saldo-=(valor+origem.tarifa)

def depositar(origem,valor):
    origem.saldo+=valor

while True:
    dess=int(input("Qual ação deseja fazer?\n(1)Transferir (2)Depositar (3)Exibir Cliente (4)Exibir Bancos Parceiros"))
    match dess:
        case 1:
            valor= int(input("Qual valor depositar em outro banco? "))
            banco= int(input("Em qual banco? \n(1)Banco União Financeira (2)Banco Central do Cerrado (3)Banco da Serra Dourada"))
            match banco:
                case 1:
                    bancoEsc=BancoUniãoFinanceira
                case 2:
                    bancoEsc=BancoCentraldoCerrado
                case 3:
                    bancoEsc=BancodaSerraDourada
            realizar_transferencia(mario,bancoEsc,valor)
        case 2:
            valor= int(input("Qual valor depositar na conta? "))
            depositar(mario,valor)
        case 3:
            mostrar_saldo(mario)
        case 4:
            print(BancoCentraldoCerrado)
            print(BancoUniãoFinanceira)
            print(BancodaSerraDourada)
