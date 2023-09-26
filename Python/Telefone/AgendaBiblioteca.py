import os
agenda = [
    ["Djonga","9998-3324"],
    ["Coringa","9978-3744"],
    ["Larissa Manuela","3398-3124"]
]
Nagenda = []

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def add():
    name=input("Digite o nome do contato: ")
    numr=input("Digite o número do contato: ")
    Nagenda.append(name)
    Nagenda.append(numr)
    agenda.append(Nagenda)
    cls()

def read():
    print("Agenda atual\n---------------------------")
    if len(agenda)==0:
        print("Você tem 0 contatos.")
    else:
        for i in range(len(agenda)):
            print(i,agenda[i])
            i=0

def edit():
    cls()
    print("\n---------------------------\nQual contato deseja editar? \n---------------------------")
    read()
    dess=int(input())
    name=input("Novo nome: ")
    numr=input("Novo número: ")
    agenda.pop(dess)
    Nagenda.append(name)
    Nagenda.append(numr)
    agenda.insert(dess,Nagenda)
    cls()
    read()
    input("Processo concluído.\n---------------------------\nPressione qualquer tecla....")
    cls()

def dele():
    read()
    if len(agenda)==0:
        print("Sem contatos para excluir.")
        input("------------------------------\nProcesso concluído.\nPressione qualquer tecla....\n------------------------------\n")
        # break
    else:
        dess=int(input("------------------------------\nQual contato excluir? "))
        agenda.pop(dess)
        cls()
        read()
        input("------------------------------\nProcesso concluído.\nPressione qualquer tecla....\n------------------------------")
    cls()

def clear():
    agenda.clear()
    cls()

def AgendaClear():
    Nagenda.clear()