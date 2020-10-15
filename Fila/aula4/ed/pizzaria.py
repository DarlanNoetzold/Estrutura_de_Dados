
from ed.fila import Fila


class Pedido:

    def __init__(self, pizza):
        self.pizza = pizza

    def __repr__(self):
        return self.pizza


def main():
    pizzaria = Fila()

    pedido1 = Pedido("Muçarela")
    pedido2 = Pedido("Calabresa")
    pedido3 = Pedido("Marguerita")
    pedido4 = Pedido("Rúcula")

    print("Recebendo pedido {}".format(pedido1))
    pizzaria.entrar(pedido1)
    
    print("Recebendo pedido {}".format(pedido2))
    pizzaria.entrar(pedido2)

    print("Recebendo pedido {}".format(pedido3))
    pizzaria.entrar(pedido3)

    pedido = pizzaria.sair()
    print("Fazendo pizza: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.vazia))

    pedido = pizzaria.sair()
    print("Fazendo pizza: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.vazia))


    pedido = pizzaria.sair()
    print("Fazendo pizza: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.vazia))




main()












