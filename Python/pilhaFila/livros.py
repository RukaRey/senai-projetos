pilhas=[
    ["Romance",("A Casa das Sete Mulheres"," Letícia Wierzchowski"),("Amor nos Tempos do Cólera","Gabriel García"),"O Morro dos Ventos Uivantes","Emily Brontë"],
    ["Comédia",("As Aventuras de Alice no País das Maravilhas","Lewis Carroll"),("O Guia do Mochileiro das Galáxias","Douglas Adams")],
    ["História",("O Século XX","Eric Hobsbawm"),("Uma Breve História da Humanidade","Yuval Noah Harari")]
]
remember=[
    [],#estante
]
import os

def addPilha():
    dess=int(input("Adicionar livro á qual pilha? "))
    novoLivro=input("Nome do livro? ")
    novoAutor=input("Nome do autor? ")
    pilhas[dess].insert(1, ((novoLivro, novoAutor)))

def remLivro():
    dess=int(input("Remover livro de qual pilha? "))
    if dess>len(pilhas):
        print("Não tem nenhuma pilha ali!")
    else:
        est=(pilhas[dess][1])
        remember[0].insert(0,est)
        pilhas[dess].pop(1)

def saveLivro():
    saveL=-1
    if remember[0]<1:
        print("Não tem nenhum livro na estante!")
    else:
        for i in remember[0]:
            saveL=saveL+1
            print(saveL,i)
        dess=int(input("Qual livro salvar? "))
        if dess>len(remember[0]):
            print("Nenhum livro númerado!")
        else:
            save=remember[0][dess]
            desc=int(input("Devolver livro á qual pilha? "))
            if desc>len(pilhas):
                print("Não tem nenhuma pilha ali!")
            else:
                pilhas[desc].insert(1, save)

def showPilha():
    # Mostra o livro do topo sem remover.
    pilhaNum=-1
    for i in pilhas:
        pilhaNum=pilhaNum+1
        print(pilhaNum,pilhas[pilhaNum][0])

def NewPilha():
    # criar nova pilha de livros
    while(True):
        novoNome=input("Nome da nova pilha?(Digite 'N' para parar)")

        if novoNome=="N":
            break
        else:
            novaPilha=[novoNome]
            pilhas.append(novaPilha)

def lookPilha():
    qu=int(input("Qual pilha olhar?"))
    if qu>len(pilhas):
        print("Não tem nenhuma pilha ali")
    else:
        print("\nLivro no topo:",pilhas[qu][1])
        print("Quantos livros tem na pilha? ")
        print("Tem ", (len(pilhas[qu]))-1," Livros na pilha de",pilhas[qu][0],".")

while(True):
    os.system("cls")
    decisao=int(input("Você se encontra na sua biblioteca pessoal. O que deseja fazer? \n(1)Adicionar um livro\n(2)Pegar um livro\n(3)Devolver um livro\n(4)Admirar pilha de livros\n(5)Criar nova pilha\n(6)Sair"))
    match decisao:
        case 1:
            os.system("cls")
            showPilha()
            addPilha()
            input("Pressione qualquer tecla pra continuar....")
        case 2:
            os.system("cls")
            showPilha()
            remLivro()
            input("Pressione qualquer tecla pra continuar....")
        case 3:
            os.system("cls")
            showPilha()
            saveLivro()
            input("Pressione qualquer tecla pra continuar....")
        case 4:
            os.system("cls")
            showPilha()
            lookPilha()
            input("Pressione qualquer tecla pra continuar....")
        case 5:
            os.system("cls")
            NewPilha()
            input("Pressione qualquer tecla pra continuar....")
        case 6:
            break
        case _:
            os.system("cls")
            pass