import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de grid()")

rotulo1 = tk.Label(janela, text="Rótulo 1")
rotulo2 = tk.Label(janela, text="Rótulo 2")
botao1 = tk.Button(janela, text="Botão 1")

# Organiza os widgets em uma grade
rotulo1.grid(row=2, column=1)
rotulo2.grid(row=0, column=1)
botao1.grid(row=1, column=0, columnspan=2)

janela.mainloop()