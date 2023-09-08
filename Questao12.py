class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

class Arvore:
    def __init__(self):
        self.raiz = None
    
    
    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)
    
    def _remover_recursivo(self, no_atual, valor):
        if no_atual is None:
            return None
        
        if valor < no_atual.valor:
            no_atual.no_esquerdo = self._remover_recursivo(no_atual.no_esquerdo, valor)
        elif valor > no_atual.valor:
            no_atual.no_direito = self._remover_recursivo(no_atual.no_direito, valor)
        else:
            if no_atual.no_esquerdo is None:
                return no_atual.no_direito
            elif no_atual.no_direito is None:
                return no_atual.no_esquerdo
            
            substituto = self._encontrar_minimo(no_atual.no_direito)
            no_atual.valor = substituto.valor
            no_atual.no_direito = self._remover_recursivo(no_atual.no_direito, substituto.valor)
        
        return no_atual
    
    def _encontrar_minimo(self, no_atual):
        while no_atual.no_esquerdo:
            no_atual = no_atual.no_esquerdo
        return no_atual
    
    
arvore = Arvore()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

print("Árvore antes da remoção:", arvore.travessia_inordem())

arvore.remover(5)
print("Árvore após a remoção:", arvore.travessia_inordem())
