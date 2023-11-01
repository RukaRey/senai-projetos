class Livro:
    def __init__(self,titulo,autor,numPaginas,paginaAtual):
        self.titulo=titulo
        self.autor=autor
        self.numPaginas=numPaginas
        self.paginaAtual=paginaAtual

    def proxPag(self):
        if self.paginaAtual == self.numPaginas:
            input("Fim")
        else:
            self.paginaAtual+=1
    
    def pagAnte(self):
        if self.paginaAtual == 1:
            input("Começo")
        else:
            self.paginaAtual-=1

livro1=Livro("Paixões e romances","Pedro Cinurinha",300,290)
livro2=Livro("Piadas inexplicáveis em caso de apreensão policial","Palhaço Piadinha",22,1)

livroAt=livro2
while True:
    print(f"Estou atualmente na página {livroAt.paginaAtual} do livro {livroAt.titulo}.")
    dess=input("O que fazer? \n(1)Passar Página (2)Voltar página")
    match dess:
        case '1':
            livroAt.proxPag()
        case '2':
            livroAt.pagAnte()