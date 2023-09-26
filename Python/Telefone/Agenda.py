import os
import AgendaBiblioteca as H

while(True):
    H.cls()
    dess=int(input("Agenda!\nFunções:\n(1)Adicionar contato\n(2)Editar contato\n(3)Ler contatos\n(4)Excluir contato\n(5)Limpar contatos\n(6)Sair"))
    H.cls()

    match dess:
        case 1:
            H.read()
            H.add()
            H.cls()
            H.read()
            input("Processo concluído.\n---------------------------\nPressione qualquer tecla....")
            H.AgendaClear()
        case 2:
            H.edit()
        case 3:
            H.read()
            input("Processo concluído.\n---------------------------\nPressione qualquer tecla....")
        case 4:
            H.cls()
            H.dele()
        case 5:
            H.clear
        case 6:
            break
        case _:
            input("Comando inválido!")