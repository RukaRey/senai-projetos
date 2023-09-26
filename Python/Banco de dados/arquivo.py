nome_do_arquivo="Frases.txt"

with open(nome_do_arquivo,"w") as txt:
    txt.write("Lembre-se do que te faz humano.\n")
    txt.write("Do que te faz completo.\n")


# read(): Lê o arquivo inteiro
with open(nome_do_arquivo,"r") as txt:
    text= txt.read()

print(text)
# readline(): Lê uma linha de cada vez, geralmente usado em loops


# readlines(): Lê todas as linhas de um arquivo e armazena em uma lista
nome_arquivo = "arquivo.txt"

with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()# <------Criando lista

for linha in linhas:# <----------Lendo a lista
    print(linha, end='')
#
#
