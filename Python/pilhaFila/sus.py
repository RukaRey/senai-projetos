sus=["Seu Gerônimo","Dona Aparecida","Empreiteiro Miguel"],
ficha=1
# quantos pacientes na fila
print(len(sus))
# mostrar pacientes na fila
print(sus)

# Gera uma ficha que é incrementada em ordem crescente toda vez que é chamada.
def gerarFicha():
    global ficha
    print(f"Sua ficha será {ficha}.")
    ficha += 1
    return ficha

# chamar próximo paciente
def chamarProx():
    sus[0].pop(0)
    sus[1].pop(0)

# adiciona novo paciente com ficha 
def novoPaciente():
    PName=input("Qual o nome do novo paciente? ")
    sus.insert(-1,PName)
    gerarFicha()
        
def adiantarPaciente():
    chamarNome=input("Chamar qual paciente? ")
    for i in range(len(sus)):
        if chamarNome==sus[i]:
            print(f'"Paciente {chamarNome}"! O paciente foi atendido.')
            sus.remove(chamarNome)
        else:
            print(f"O paciente {chamarNome} não está presente.")


novoPaciente()
adiantarPaciente()
