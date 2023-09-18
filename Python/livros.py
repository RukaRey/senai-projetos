pilhas=[
    ["Romance","A Casa das Sete Mulheres"," Letícia Wierzchowski","Amor nos Tempos do Cólera","Gabriel García","O Morro dos Ventos Uivantes","Emily Brontë"],
    ["Comédia","As Aventuras de Alice no País das Maravilhas","Lewis Carroll","O Guia do Mochileiro das Galáxias","Douglas Adams"],
    ["História","O Século XX","Eric Hobsbawm","Uma Breve História da Humanidade","Yuval Noah Harari"]
]
remember=[
    [],#estante
    []#memoria
]


def addPilha():
    dess=int(input("Qual pilha? "))
    novoLivro=input("Nome do livro? ")
    novoAutor=input("Nome do autor? ")
    pilhas[dess].insert(1, novoAutor)
    pilhas[dess].insert(1, novoLivro)

def remLivro():
    dess=int(input("Qual pilha? "))
    est=(pilhas[dess][1],pilhas[dess][2])
    remember[0].append(est)
    remember[1].insert(0,dess)
    pilhas[dess].pop(1)
    pilhas[dess].pop(1)

def saveLivro():
    saveL=-1
    for i in remember[0]:
        saveL=saveL+1
        print(saveL,i)
        dest=remember[1][0]
    dess=int(input("Qual livro salvar? "))
    january=remember[0][dess]
    decem=dess-1
    december=remember[0][decem]
    pilhas[dest].insert(0,january)
    pilhas[dest].insert(0,december)
    


def showPilha():
    # Mostra o livro do topo sem remover.
    pilhaNum=-1
    for i in pilhas:
        pilhaNum=pilhaNum+1
        print(pilhas[pilhaNum][0])

def HMpilha():
    # Exibe o número total de livros em uma pilha.
    showPilha()
    liv=int(input("Qual pilha? "))
    print("Tem ", (len(pilhas[liv]))-1," Livros na pilha de",pilhas[liv][0],".")

def NewPilha():
    # criar nova pilha de livros
    while(True):
        novoNome=input("Nova pilha?")

        if novoNome=="N":
            break
        else:
            novaPilha=[novoNome]
            pilhas.append(novaPilha)

def lookPilha():
    qu=int(input("Qual pilha?"))
    print(pilhas[qu][0],"\nLivro: ",pilhas[qu][1],"\nAutor: ",pilhas[qu][2])
# mostrar todas as pilhas de livro
# addPilha()
remLivro()
# lookPilha()
saveLivro()
showPilha()
