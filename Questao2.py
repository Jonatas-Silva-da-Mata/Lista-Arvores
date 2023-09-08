class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

class Arvore:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)
    
    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.no_esquerdo is None:
                no_atual.no_esquerdo = No(valor)
            else:
                self._inserir_recursivo(no_atual.no_esquerdo, valor)
        else:
            if no_atual.no_direito is None:
                no_atual.no_direito = No(valor)
            else:
                self._inserir_recursivo(no_atual.no_direito, valor)

arvore = Arvore()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
