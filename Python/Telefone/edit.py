import os

# 1add
# 2edit
# 3read
# 4del
# 5clean
agenda = [
    ["Djonga","9998-3324"],
    ["Coringa","9978-3744"],
    ["Larissa Manuela","3398-3124"]
]

Nagenda = []

def edit():
    os.system("cls")

    print("Qual contato deseja editar? \n---------------------------")
    # read()
    for i in range(len(agenda)):
        print(i,agenda[i])
    dess=int(input())
    name=input("Novo nome: ")
    numr=input("Novo número: ")
    agenda.pop(dess)
    Nagenda.append(name)
    Nagenda.append(numr)
    agenda.insert(dess,Nagenda)

    os.system("cls")
    # read()
    for i in range(len(agenda)):
        print(agenda[i])
    input("Processo concluído.\n---------------------------\nPressione qualquer tecla....")



edit()