class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

def verificar_arvore_de_busca(no_atual, min_valor=float('-inf'), max_valor=float('inf')):
    if no_atual is None:
        return True
    
    if no_atual.valor <= min_valor or no_atual.valor >= max_valor:
        return False
    
    return (verificar_arvore_de_busca(no_atual.no_esquerdo, min_valor, no_atual.valor) and
            verificar_arvore_de_busca(no_atual.no_direito, no_atual.valor, max_valor))

# Exemplo de uso
raiz = No(10)
raiz.no_esquerdo = No(5)
raiz.no_direito = No(15)
raiz.no_esquerdo.no_esquerdo = No(3)
raiz.no_esquerdo.no_direito = No(7)

e_arvore_de_busca = verificar_arvore_de_busca(raiz)
print("É uma árvore de busca válida?", e_arvore_de_busca)
