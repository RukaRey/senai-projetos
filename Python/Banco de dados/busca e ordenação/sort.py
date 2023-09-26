alfa=[]
delta=[]

for i in range(1,6):
    pessoa=input(f"Qual o nome da pessoa {i}?")
    alfa.append(pessoa)
    delta.append(pessoa)
    delta.sort()
    print(delta)

print("Lista original:")
print(alfa)
print("Lista em ordem alfabética:")
print(delta)
