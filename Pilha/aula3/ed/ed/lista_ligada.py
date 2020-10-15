class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None

class ListaLigada:

    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio
    
    @property
    def quantidade(self):
        return self._quantidade
    
    def inserir_no_inicio(self, conteudo):
        celula = Celula(conteudo)
        celula.proximo = self._inicio
        self._inicio = celula
        self._quantidade += 1

    def inserir(self, posicao, conteudo):
        if posicao == 0:
            self.inserir_no_inicio(conteudo)
            return
        celula_anterior = self._celula(posicao - 1)
        celula = Celula(conteudo)
        celula.proximo = celula_anterior.proximo
        celula_anterior.proximo = celula
        self._quantidade += 1

    def remover_do_inicio(self):
        removido = self._inicio
        self._inicio = self._inicio.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def remover(self, posicao):
        if posicao == 0:
            return self.remover_do_inicio()
        celula_anterior = self._celula(posicao - 1)
        removido = celula_anterior.proximo
        celula_anterior.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def item(self, posicao):
        celula = self._celula(posicao)
        return celula.conteudo

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        celula_atual = self.inicio
        for i in range(0, posicao):
            celula_atual = celula_atual.proximo
        return celula_atual

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError(
            "Posição inválida {}".format(posicao))

    def imprimir(self):
        celula_atual = self.inicio
        for i in range(0, self.quantidade):
            print(celula_atual.conteudo)
            celula_atual = celula_atual.proximo



































































