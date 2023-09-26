# Está funcionando! Graças ao robô.
Nomes="nomes-aniver.txt"
list=[]

while(True):
    name=input("Nome: ")
    if name=="0":
        break
    else:
        with open(Nomes,"a",encoding='utf-8') as nomes:
            birth=input("Aniversário: ")
            nomes.write(name + " ")
            nomes.write(birth + "\n")

with open(Nomes, "r") as arquivo:
    users = arquivo.readlines()

for i in users:
    variaveis=i.split()    

    linhas_variaveis=[variaveis[0],variaveis[1]]
    list.append(linhas_variaveis)

print(users[0],users[1])



# # Se o usuário digitar Y, o arquivo é limpo.
# if input("Limpar? ")=="Y":
#     with open(Nomes, "w") as nomes:
#         nomes.write(" ")
# else:
#     pass