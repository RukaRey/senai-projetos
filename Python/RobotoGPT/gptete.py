import tkinter as tk
import tkinter.font as tkfont
from PIL import Image, ImageTk

def fechar_janelas(janelas):
    for janela in janelas:
        janela.destroy()


def verificar_login():
    usuario = entryUser.get()
    senha = entryPass.get()

    # Verificar se o usuário e senha estão corretos (pode adicionar seu próprio sistema de autenticação aqui)
    if usuario == "admin" and senha == "0000":
        parabens = tk.Label(janela, foreground="green", text="Bem vindo!            ",font=FontSize)
        parabens.place(x=0, y=150)
    else:
        falha = tk.Label(janela, foreground="#FF0000", text="Senha incorreta.",font=FontSize)
        falha.place(x=0, y=150)


janela = tk.Tk()
janela.title("Login GPT")
FontSize = tkfont.Font(size=9)
janela.configure(bg="pink")


largura = 500  # Define a altura e largura inicial da tela.
altura = 250
janela.geometry(f"{largura}x{altura}")

bcg= Image.open("forro.png")
bcg_tk = ImageTk.PhotoImage(bcg)
label_fundo = tk.Label(janela, image=bcg_tk)
label_fundo.place(relwidth=1, relheight=1, x=200)  # Cobrir toda a janela

janela.minsize(largura, altura)  # Define o tamanho mínimo como 500x250px, 
janela.maxsize(largura, altura)  # trancando ela na definição inicial.

userLabel = tk.Label(janela, text="Usuário:")
passLabel = tk.Label(janela, text="Senha:")
entryUser = tk.Entry(janela)
entryPass = tk.Entry(janela, show="*")
buttonLogin = tk.Button(janela, text="Login", command=verificar_login)

userLabel.place(x=50, y=20)
entryUser.place(x=100, y=50)
passLabel.place(x=50, y=80)
entryPass.place(x=100, y=110)
buttonLogin.place(x=183, y=140)
buttonLogin.configure(fg="pink")

janela.mainloop()
verificar_login()