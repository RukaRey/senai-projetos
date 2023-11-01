class Cinema:
    def __init__(self,nome,capacidade,ingressos_vendidos):
        self.nome=nome
        self.capacidade=capacidade
        self.ingressos_vendidos=ingressos_vendidos

    def vender_ingressos(self,qte):
        if qte>self.capacidade:
            input("Capacidade excedida.")
        else:
            self.capacidade-=qte
    
    def cancelar_venda(self,qte):
        if self.capacidade>=300:
            input("Nenhum ingresso para cancelar.")
            self.capacidade=300
        else:
            self.capacidade+=qte
    
    def lugares_disponiveis(self):
        return self.capacidade
    
cinema1=Cinema("Alameda",300,22)
cinema2=Cinema("Barbenheimer",4000, 3220)


cineAtual=cinema1
while True:
    print(f"Gerenciando o cinema {cineAtual.nome}.")
    dess=input("Oque fazer? \n(1)Vender ingresso (2)Cancelar compra (3)Checar capacidade")
    match dess:
        case '1':
            qte=int(input("Vender quantos ingressos? "))
            cineAtual.vender_ingressos(qte)
        case '2':
            qte=int(input("Cancelar quantas compras? "))
            cineAtual.cancelar_venda(qte)
        case '3':
            print(f"Capacidade disponível: {cineAtual.lugares_disponiveis()}.")