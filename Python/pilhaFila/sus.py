import os

sus=["Seu Gerônimo","Dona Aparecida","Empreiteiro Miguel"]
ficha=4

def mostrarFila():
    print(f"Pacientes: {sus}")
    if len(sus)==1:
        print(f"Tem {len(sus)} paciente na fila.")
    else:
        print(f"Tem {len(sus)} pacientes na fila.")

def gerarFicha():
    global ficha
    print(f"Sua ficha será {ficha}.")
    ficha += 1
    return ficha

def chamarProx():
    if len(sus)==0:
        print("Que milagre, não tem ninguém na fila.")
    else:
        print(f'"Paciente {sus[0]}"! O paciente foi atendido.')
        sus.pop(0)

def novoPaciente():
    PName=input("Qual o nome do novo paciente? ")
    sus.append(PName)
    gerarFicha()
        
def adiantarPaciente():
    print(f"Pacientes: {sus}")
    chamarNome=input("Chamar qual paciente? ")
    if chamarNome in sus:
        print(f'"Paciente {chamarNome}"! O paciente foi atendido.')
        sus.remove(chamarNome)
    else:
        print(f"O paciente {chamarNome} não está presente.")

while(True):
    os.system("cls")
    print("Posto de saúde\nJá tem uma fila de pacientes aguardando atendimento. O que fazer?")
    dess=int(input("(1)Próximo paciente!\n(2)Novo paciente\n(3)Chamar paciente\n(4)Olhar fila\n(5)Fim do expediente"))
    match dess:
        case 1:
            chamarProx()
            input("E agora....")
        case 2:
            novoPaciente()
            input("E agora....")
        case 3:
            adiantarPaciente()
            input("E agora....")
        case 4:
            mostrarFila()
            input("E agora....")
        case 5:
            os.system("cls")
            print("Mais um dia de trabalho.")
            break
        case _:
            os.system("cls")
            input("Ah, calma. Me distraí.")
