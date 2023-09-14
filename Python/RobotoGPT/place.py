import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de place()")

rotulo = tk.Label(janela, text="Rótulo")
botao = tk.Button(janela, text="Botão")

# Posiciona o rótulo e o botão usando coordenadas x e y
rotulo.place(x=200, y=20)
botao.place(x=100, y=50)

janela.mainloop()