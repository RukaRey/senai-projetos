import tkinter as tk

def inserir_texto():
    texto = "Texto que será inserido na caixa de texto."
    caixa_texto.delete("1.0", tk.END)  # Limpa o conteúdo atual
    caixa_texto.insert(tk.END, texto)  # Insere o novo texto

janela = tk.Tk()
janela.title("Caixa de Texto com Botão")

caixa_texto = tk.Text(janela, height=10, width=40)
caixa_texto.pack()

botao = tk.Button(janela, text="Mostrar Texto", command=inserir_texto)
botao.pack()

janela.mainloop()
