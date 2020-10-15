from ed.lista_ligada import ListaLigada, Celula

class Loja:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "{}\n  {}".format(self.nome, self.endereco)


def main():
    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 300")
    loja2 = Loja("Hortifruti", "Rua do Pomar, 1300")
    loja3 = Loja("Padaria Pão da Hora", "Av das Flores, 344")
    loja4 = Loja("Supermercado da Saúde", "Alameda das Jabuticabeiras, 500")
    loja5 = Loja("Mini mercado da Fazenda", "Rua da Fazenda, 98")

    lista = ListaLigada()
    lista.inserir_no_inicio(loja1)
    lista.inserir_no_inicio(loja2)
    lista.inserir(2, loja3)
    lista.inserir(0, loja4)
    lista.inserir(1, loja5)

    print(lista.quantidade)
    lista.imprimir()
    removido = lista.remover_do_inicio()
    print("\nRemovido: {}".format(removido))
    print("")

    print(lista.quantidade)
    lista.imprimir()
    removido = lista.remover(2)
    print("\nRemovido: {}".format(removido))
    print("")
    print(lista.quantidade)
    lista.imprimir()

    print(lista.quantidade)
    lista.imprimir()
    removido = lista.remover(2)
    print("\nRemovido: {}".format(removido))
    print("")
    print(lista.quantidade)
    lista.imprimir()

    print(lista.quantidade)
    lista.imprimir()
    removido = lista.remover(0)
    print("\nRemovido: {}".format(removido))
    print("")
    print(lista.quantidade)
    lista.imprimir()

main()
