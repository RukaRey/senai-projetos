import calc_Bibl as c
import os

loopSec=True
Trueloop=True

while(Trueloop==True):

    os.system("cls")
        
    print("Calculadora, escolha sua operação:")
    print("---------------------------------\n1)Soma\n2)Subtração\n3)Multiplicação\n4)Divisão\n5)Potenciação\n6)Radiciação\n---------------------------------")

    escolha=int(input())

    a=int(input("Primeiro número:"))
    b=int(input("Segundo número:"))
    if escolha==1:
        resul=c.soma(a,b)
    elif escolha==2:
        resul=c.subst(a,b)
    elif escolha==3:
        resul=c.mult(a,b)
    elif escolha==4:
        while(loopSec==True):
            if b == 0:
                print("erro")
            else:
                resul=c.div(a,b)
    elif escolha==5:
        resul=c.poten(a,b)
    elif escolha==6:
        resul=c.radia(a,b)
    else:
        print()
    
    os.system("cls")

    print("O resultado da operações foi ",resul,".")
    escolha2=input("Deseja sair?\n(1)Sim\n(2)Não")
    if escolha2=="1":
        Trueloop=False
    else:
        print()
            
print("Obrigado.")