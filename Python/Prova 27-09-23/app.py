'''
LUCIANO GOMES DE FARIA          TURNO: TARDE
'''

import os
os.system('cls')

# Valores pré-estabelicidos para facilitar testagem:
estac=[
    {'placa':'QTE-0632','marca':'Chefrolet','ano':2014,'preco':38000,'kmr':1000,'lkm':2000},
    {'placa':'QTE-2432','marca':'Uno','ano':2007,'preco':32000,'kmr':500,'lkm':200},
    {'placa':'QTE-0431','marca':'Chefrolet','ano':2004,'preco':55000,'kmr':100,'lkm':200},
    {'placa':'QTE-0432','marca':'Ford','ano':2010,'preco':30000,'kmr':2000,'lkm':1000}
]

def addCar():
    os.system('cls')
    check=False
    print("-"*69)
    print("Registrando novo carro.\n Por favor insira correntamente as seguintes informações:")
    print("-"*69)
    placa=input("Placa: ")
    for car in estac:
        check=car['placa']
        if car['placa']==placa:
            print("Placa já registrada. Erro no sistema.")
            check=True
    if check==True:
        pass
    else:
        marca=input("Marca: ")
        ano=int(input("Ano: "))
        preco=int(input("Preço: "))
        kmr=int(input("Km rodados: "))
        lkm=int(input("Limite de uso: "))
        carroNovo = {'placa':placa,'marca':marca,'ano':ano,'preco':preco,'kmr':kmr,'lkm':lkm}
        estac.append(carroNovo)
    print("-"*69)
    print("Insira qualquer caractere para prosseguir....")
    input("-"*69)

def remCar():
    no=0
    print("-"*69)
    removed=input("Qual a placa do carro que irá ser removido? ")
    for car in estac:
            if car['placa']==removed:
                print("-"*69)
                print(f"{car['placa']}\t{car['marca']}\t{car['ano']}\t\tR${'{:.2f}'.format(car['preco'])}\t{car['kmr']}\t{car['lkm']}")
                print("-"*69)
                no=1
    if input("Tem certeza? (1) para continuar")=='1':
        for car in estac:
            if car['placa']==removed:
                estac.remove(car)
                print("-"*69)
                print("Carro removido do sistema.")
    else:
        print("Processo interrompido.")
    if no==0:
        print("Carro não registrado. Erro no sistema.")
    print("-"*69)
    print("Insira qualquer caractere para prosseguir....")
    input("-"*69)

def calcValue():
    os.system('cls')
    print("-"*69)
    print("Valor total em estoque: ")
    print("PLACA\t\tMARCA\t\t\tPREÇO")
    print("-"*69)
    soma=0
    if len(estac)==0:
        print("Não há nenhum carro em estoque.")
    else:
        for car in estac:
            soma=soma+car['preco']
        for car in estac:  
                if len(car['marca'])<8:
                    car['marca']=car['marca']+"\t"
                    print(f"{car['placa']}\t{car['marca']}\t\tR${'{:.2f}'.format(car['preco'])}")
                else:
                    print(f"{car['placa']}\t{car['marca']}\t\tR${'{:.2f}'.format(car['preco'])}")
    print("-"*69)
    print(f"O valor total é R${'{:.2f}'.format(soma)}.")
    print("Insira qualquer caractere para prosseguir....")
    input("-"*69)
    
def showCars(): 
    if len(estac)==0:
        print("Nenhum carro no estacionamento.")
    else:
        print("PLACA\t\tMARCA\t\tANO\tPREÇO\t\tKM\tUSO")
        print("-"*69)
        for car in estac:  
            if len(car['marca'])<8:
                # car['marca']=car['marca']+"\t"
                print(f"{car['placa']}\t{car['marca']}\t\t{car['ano']}\tR${'{:.2f}'.format(car['preco'])}\t{car['kmr']}\t{car['lkm']}")
            elif len(car['marca'])>8:
                print(f"{car['placa']}\t{car['marca']}\t{car['ano']}\tR${'{:.2f}'.format(car['preco'])}\t{car['kmr']}\t{car['lkm']}")
            else:
                print(f"{car['placa']}\t{car['marca']}\t{car['ano']}\t\tR${'{:.2f}'.format(car['preco'])}\t{car['kmr']}\t{car['lkm']}")

def frailCar():
    os.system('cls')
    desg=0
    for car in estac:
        if car['kmr']>=car['lkm']:
            desg=desg+1
    print("-"*69)
    print("Os seguintes carros estão desgastados:")
    print("-"*69)
    if len(estac)==0 or desg<1:
        print("Não há nenhum carro desgastado.")
    else:
        for car in estac:
            if car['kmr']>=car['lkm']:
                print(f"{car['placa']}\t{car['marca']}\t{car['ano']}\t\tR${'{:.2f}'.format(car['preco'])}\t{car['kmr']}\t{car['lkm']}")
    print("-"*69)
    print("Insira qualquer caractere para prosseguir....")
    input("-"*69)

def searchCar():
    no=0
    os.system('cls')
    print("-"*69)
    placa=input("Qual a placa do carro que deseja encontrar? ")
    for car in estac:
        if car['placa']==placa:
            print("Carro encontrado:")
            print("-"*69)
            print("PLACA\t\tMARCA\t\tANO\tPREÇO\t\tKM\tUSO")
            print("-"*69)
            if len(car['marca'])<8:
                # car['marca']=car['marca']+"\t"
                print(f"{car['placa']}\t{car['marca']}\t\t{car['ano']}\tR${'{:.2f}'.format(car['preco'])}\t{car['kmr']}\t{car['lkm']}")
            elif len(car['marca'])>8:
                print(f"{car['placa']}\t{car['marca']}\t{car['ano']}\tR${'{:.2f}'.format(car['preco'])}\t{car['kmr']}\t{car['lkm']}")
            else:
                print(f"{car['placa']}\t{car['marca']}\t{car['ano']}\t\tR${'{:.2f}'.format(car['preco'])}\t{car['kmr']}\t{car['lkm']}")
            no=no+1   
    if no==0:
        print("Carro não registrado no sistema.")
    print("-"*69)
    print("Insira qualquer caractere para prosseguir....")
    input("-"*69)

while(True):
    os.system('cls')
    print("-"*69)
    print("Bem-vindo.")
    print("Carros no estacionamento:")
    print("-"*69)
    showCars()
    print("-"*69)
    dess=int(input("O'que deseja fazer? \n(1)Adicionar veículo\t(2)Remover veículo\n(3)Buscar veículo\t(4)Valor em Estoque\n(5)Veículos desgastados\t(6)Sair"))
    match dess:
        case 1:
            addCar()
        case 2:
            os.system('cls')
            showCars()
            remCar()
        case 3:
            searchCar()
        case 4:
            calcValue()
        case 5:
            frailCar()
        case 6:
            print("-"*69)
            print("Obrigado pela preferência.")
            print("-"*69)
            break
        case _:
            print("-"*69)
            print("Comando inválido.")
            print("Insira qualquer caractere para prosseguir....")
            input("-"*69)