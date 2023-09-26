# dicionario = {'banana': 3, 'maçã': 1, 'laranja': 2}
# dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1]))

# print(dicionario_ordenado)

clientela = {}

for i in range(1,6):
    cliente=input("Qual é o nome do cliente? ")
    clientela[cliente]=input("Ficha de número: ")
    ordemNum = dict(sorted(clientela.items(), key=lambda item: item[1]))
    ordemAlfa = dict(sorted(clientela.items(), key=lambda item: item[0]))
    print(ordemNum,ordemAlfa)

print(clientela)