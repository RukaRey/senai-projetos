import os, random

class Personagem():
    def __init__ (self,start_x,start_y):
        self.pos_x = start_x
        self.pos_y = start_y
    
    def moveUp(self):
        global pontuação
        if self.pos_y>=5:
            print("prede")
            pass
        else:
            self.pos_y+=1
            pontuação += 0.1
    def moveDown(self):
        global pontuação
        if self.pos_y<=-5:
            print("prede")
            pass
        else:
            self.pos_y-=1
            pontuação += 0.1
    def moveLeft(self):
        global pontuação
        if self.pos_x<=-5:
            print("prede")
            pass
        else:
            self.pos_x-=1
            pontuação += 0.1
    def moveRight(self):
        global pontuação
        if self.pos_x>=5:
            print("prede")
            pass
        else:
            self.pos_x+=1
            pontuação += 0.1
    def status(self):
        print(f"Você está em {p.pos_x},{p.pos_y}.\nO inimigo está em {r.pos_x},{r.pos_y}.\nVocê sobreviveu por {pontuação} horas.")
        

p = Personagem(0,0)
randor=random.randint(-5,5)
r = Personagem(randor,randor)
pontuação = 0.0

while True:
    os.system('cls')
    p.status()
    escolha=input("Para qual direção?\n(1)Cima (2)Baixo (3)Esquerda (4)Direita")
    match escolha:
        case '1':
            os.system('cls')
            p.moveUp()
        case '2':
            os.system('cls')
            p.moveDown()
        case '3':
            os.system('cls')
            p.moveLeft()
        case '4':
            os.system('cls')
            p.moveRight()
        case _:
            break
    
    if r.pos_x==5:
        enemy=random.randint(1,3)
        match enemy:
            case 1:
                os.system('cls')
                r.moveUp()
            case 2:
                os.system('cls')
                r.moveDown()
            case 3:
                os.system('cls')
                r.moveLeft()
    elif r.pos_x==-5:
        enemy=random.randint(1,3)
        match enemy:
            case 1:
                os.system('cls')
                r.moveUp()
            case 2:
                os.system('cls')
                r.moveDown()
            case 3:
                os.system('cls')
                r.moveRight()
    elif r.pos_y==-5:
        enemy=random.randint(1,3)
        match enemy:
            case 1:
                os.system('cls')
                r.moveUp()
            case 2:
                os.system('cls')
                r.moveDown()
            case 3:
                os.system('cls')
                r.moveRight()
    elif r.pos_y==-5:
        enemy=random.randint(1,3)
        match enemy:
            case 1:
                os.system('cls')
                r.moveDown()
            case 2:
                os.system('cls')
                r.moveLeft()
            case 3:
                os.system('cls')
                r.moveRight()
    else:
        enemy=random.randint(1,3)
        match enemy:
            case 1:
                os.system('cls')
                r.moveUp()
            case 2:
                os.system('cls')
                r.moveDown()
            case 3:
                os.system('cls')
                r.moveRight()
            case 3:
                os.system('cls')
                r.moveLeft()
    if p.pos_x==2 and p.pos_y==5:
        input("Você encontrou um tesouro!")

    if p.pos_x==-3 and p.pos_y==5:
        input("Você encontrou um mendigo!")

    if r.pos_x==p.pos_x and r.pos_y==p.pos_y:
        input("O inimigo te alcançou!")
        break

    
os.system('cls')
print("Destino cruel. Game Over.")