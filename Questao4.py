class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

class Arvore:
    def __init__(self):
        self.raiz = None
    
    
    def calcular_altura(self):
        return self._calcular_altura_recursivo(self.raiz)
    
    def _calcular_altura_recursivo(self, no_atual):
        if no_atual is None:
            return -1  
        altura_esquerda = self._calcular_altura_recursivo(no_atual.no_esquerdo)
        altura_direita = self._calcular_altura_recursivo(no_atual.no_direito)
        return max(altura_esquerda, altura_direita) + 1

arvore = Arvore()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

altura = arvore.calcular_altura()
print("Altura da árvore:", altura)
