class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

def contar_nos(no_atual):
    if no_atual is None:
        return 0
    
    return 1 + contar_nos(no_atual.no_esquerdo) + contar_nos(no_atual.no_direito)

raiz = No(10)
raiz.no_esquerdo = No(5)
raiz.no_direito = No(15)
raiz.no_esquerdo.no_esquerdo = No(3)
raiz.no_esquerdo.no_direito = No(7)

total_nos = contar_nos(raiz)
print("Total de nós na árvore:", total_nos) 
