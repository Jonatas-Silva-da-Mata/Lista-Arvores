class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

def encontrar_valor_maximo(no_atual):
    if no_atual is None:
        return float('-inf') 
    
    max_esquerdo = encontrar_valor_maximo(no_atual.no_esquerdo)
    max_direito = encontrar_valor_maximo(no_atual.no_direito)
    
    return max(no_atual.valor, max_esquerdo, max_direito)

raiz = No(10)
raiz.no_esquerdo = No(5)
raiz.no_direito = No(15)
raiz.no_esquerdo.no_esquerdo = No(3)
raiz.no_esquerdo.no_direito = No(7)

valor_maximo = encontrar_valor_maximo(raiz)
print("Valor máximo na árvore:", valor_maximo) 