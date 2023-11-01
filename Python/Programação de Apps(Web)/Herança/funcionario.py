class Funcionario:
    def __init__(self,nome,salario):
        self.nome= nome
        self.salario= salario
    def addAumento(self,valor):
        valor= int(input("Qual o valor do aumento? "))
        self.salario+=valor
    def ganhoAnual(self):
        salarioAnual= self.salario*12
        print(f"Funcionário {self.nome} recebe {salarioAnual} por ano.")
    def exibeDados(self):
        print(f"Funcionário: {self.nome}\nSalário: {self.salario}")

class Assistente(Funcionario):
    def __init__(self,nome,salario,numMatricula):
        super().__init__(nome,salario)
        self.numMatricula= numMatricula

    def exibeDados(self):
        super().exibeDados()
        print(f"Matrícula: {self.numMatricula}")
    def setFunc(self):
        new=input("Nome do funcionário: ")
        self.nome= new
        new=int(input("Novo salário: "))
        self.salario= new
        new=int(input("Novo nº de matrícula: "))
        self.numMatricula= new        

class AssistenteTec(Assistente):
    def __init__(self,nome,salario,numMatricula):
        super().__init__(nome,salario,numMatricula)
        self.bonus= 200

    def ganhoAnual(self):
        salarioAnual= (self.salario+self.bonus)*12
        print(f"Funcionário {self.nome} recebe {salarioAnual} por ano.")
    
class AssistenteAdM(Assistente):
    def __init__(self,nome,salario,numMatricula,dia):
        super().__init__(nome,salario,numMatricula)
        self.noite=dia

    def ganhoAnual(self):
        if self.noite:
            salarioAnual= (self.salario+350)*12
            print(f"Funcionário {self.nome} recebe {salarioAnual} por ano.")
        else:
            salarioAnual= self.salario*12
            print(f"Funcionário {self.nome} recebe {salarioAnual} por ano.")

func=Funcionario("Ronaldo",1000)
assis=Assistente("Júnior",2000,22)
assisAdmin=AssistenteAdM("Júkor",300,2,False)
assisTec=AssistenteTec("Kin",990,5)

func.ganhoAnual()
func.exibeDados()