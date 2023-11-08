import os
import sqlite3

conn = sqlite3.connect('clientes.db')   # Cria a conexão com o arquivo 'clientes.db' com banco de dado
cursor = conn.cursor()                  # Representa a conexão com o servidor

# Criar uma nova tabela chamada "usuarios" caso não existe. Se já existir nada será feito
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')

# Inserir um novo registro na tabela "usuarios"
def insertUser(nome,idade):
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))

def listarUsers():
    global registros
    # Recuperando a lista de usuários
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()


    for item in registros:
        print(f"ID: {item[0]}, Nome: {item[1]}, Idade: {item[2]}")

def removeUser(id):
    cursor.execute(f"DELETE FROM usuarios WHERE id = {id}")

def updateUser(id,novoNome,novaIdade):
    cursor.execute(f"UPDATE usuarios SET nome = '{novoNome}', idade = {novaIdade} WHERE id = {id}")

while True:
    os.system('cls')
    dess=input("Opções:\n(1)Inserir usuário\t(2)Remover usuário\n(3)Listar usuários\t(4)Atualizar usuário")
    match dess:
        case '1':
            nome=input("Nome do usuário: ")
            idade=int(input("Idade do usuário: "))
            insertUser(nome,idade)
        case '2':
            listarUsers()
            id=int(input("Remover qual usuário? "))
            removeUser(id)
        case '3':
            listarUsers()
            input("")
        case '4':
            listarUsers()
            id=int(input("Qual usuário? "))
            novoNome=input("Novo nome do usuário: ")
            NovaIdade=int(input("Nova idade do usuário: "))
            updateUser(id,novoNome,NovaIdade)
        case _:
            break






# Commitar as alterações e fechar a conexão
conn.commit() # Em caso de falha na execução nenhuma alteração é realizada
conn.close()  # Fecha a conexão com o servidor