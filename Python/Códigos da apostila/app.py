import json

contas = []

if len(contas)!=0:
    with open("contas.json", "r") as arquivo:
        contas = json.load(arquivo)


def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    contas.append(conta)

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))





numero=input("Numero:")
titular= input("Nome do titular? ")
saldo= float(input("Saldo: "))
limite= float(input("Limite: "))

cria_conta(numero, titular, saldo, limite)


with open("contas.json", "a") as arquivo:
    json.dump(contas,arquivo)

extrato(contas[0])

# deposita(contas[0],340.00)

extrato(contas[0])