class TreeNode:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_nos_no_nivel(raiz, nivel_alvo):
    if raiz is None:
        return []

    
    fila = [(raiz, 0)]
    nos_no_nivel = []

    while fila:
        no, nivel_atual = fila.pop(0)

        if nivel_atual == nivel_alvo:
            nos_no_nivel.append(no.valor)
        elif nivel_atual > nivel_alvo:
            break  

        if no.esquerda:
            fila.append((no.esquerda, nivel_atual + 1))
        if no.direita:
            fila.append((no.direita, nivel_atual + 1))

    return nos_no_nivel


raiz = TreeNode(1)
raiz.esquerda = TreeNode(2)
raiz.direita = TreeNode(3)
raiz.esquerda.esquerda = TreeNode(4)
raiz.esquerda.direita = TreeNode(5)
raiz.direita.esquerda = TreeNode(6)
raiz.direita.direita = TreeNode(7)


nos_nivel_2 = encontrar_nos_no_nivel(raiz, 2)
print(nos_nivel_2)  
