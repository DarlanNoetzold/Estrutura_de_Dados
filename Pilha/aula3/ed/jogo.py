from ed.pilha import Pilha


class Fase:

    def __init__(self, cenario, pontuacao, punicao):
        self.cenario = cenario
        self.pontuacao = pontuacao
        self.punicao = punicao

    def __repr__(self):
        return self.cenario


def main():
    fases = Pilha()
    fase1 = Fase("Floresta", 300, -100)
    fase2 = Fase("Castelo", 100, -4)
    fase3 = Fase("Caverna", 400, -50)
    fase4 = Fase("Guerra", 3000, -400)

    fases.empilhar(fase1)
    fases.empilhar(fase2)
    fases.empilhar(fase3)
    fases.empilhar(fase4)

    falhou = fases.desempilhar()
    print("Falhou na fase:")
    print(falhou)
    falhou = fases.desempilhar()
    print("Falhou na fase:")
    print(falhou)
    print("Voltou para a fase")
    print(fases.topo)



main()