class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

class Arvore:
    def __init__(self):
        self.raiz = None
        
    def travessia_posordem(self):
        valores = []
        self._travessia_posordem_recursivo(self.raiz, valores)
        return valores
    
    def _travessia_posordem_recursivo(self, no_atual, valores):
        if no_atual is not None:
            self._travessia_posordem_recursivo(no_atual.no_esquerdo, valores)
            self._travessia_posordem_recursivo(no_atual.no_direito, valores)
            valores.append(no_atual.valor)

arvore = Arvore()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

valores_posordem = arvore.travessia_posordem()
print("Travessia pós-ordem:", valores_posordem)