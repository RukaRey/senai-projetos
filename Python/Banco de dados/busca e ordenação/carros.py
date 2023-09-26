import tkinter as tk

carros= [
    {'marca':'VW', 'modelo':'Gol','ano':2018,'preco':45000},
    {'marca':'Ford', 'modelo':'KA','ano':2014,'preco':38000},
    {'marca':'Honda', 'modelo':'Civic','ano':2010,'preco':40000},
    {'marca':'Honda', 'modelo':'Fit','ano':2014,'preco':48000},
]

def decidirOrdem():
    criterio=input("Ordenar em qual parâmetro? (modelo,marca,ano,preco)")
    ordem = sorted(carros, key=lambda item: item[criterio])
    print("Marca\tModelo\t\tAno\tPreço")
    print("----------------------------------------")
    for i in ordem:
        print(f"{i['marca']}\t{i['modelo']}\t\t{i['ano']}\t{i['preco']}")

def botao_clicado():
    criterio=0

janela = tk.Tk()
janela.title("Minha Interface")

largura = 500  # Define a altura e largura inicial da tela.
altura = 250
janela.geometry("500x230")
janela.maxsize(largura,altura)

botaoMarca = tk.Button(janela, text="Marca",command=)
botaoModelo = tk.Button(janela, text="Modelo")
botaoAno = tk.Button(janela, text="Ano")
botaoPreco = tk.Button(janela, text="Preço")
botaoMarca.config(command=botao_clicado)

caixa_texto = tk.Text(janela, height=11, width=40)

caixa_texto.place(x=150,y=10)
botaoMarca.place(x=50,y=10)
botaoModelo.place(x=50,y=60)
botaoAno.place(x=50,y=110)
botaoPreco.place(x=50,y=160)
janela.mainloop()



