# É uma fórmula que pega informações e executa uma ação pré setada.
# "Uma máquina para produzir alguma coisa", utilizando argumentos/parâmetros.
# Resumo: Reuso.

from datetime import datetime

now = datetime.now().hour


# Declara a função antes do programa. Uma saudação amigável quando chamada.
def saudacao(nome):
    if now >= 00 and now <=12:
        print("Bomdia",nome)
    elif now > 17:
        print("Bomnoite",nome)
    else:
        print("Bomtarde",nome)
# Chama a função com passagem de valor
saudacao("Luciano")

# Chama a função com passagem de referência
nome=input("Digite seu nome:")
saudacao(nome)