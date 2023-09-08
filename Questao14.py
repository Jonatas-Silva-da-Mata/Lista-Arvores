class TreeNode:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_caminho(raiz, valor_alvo):
    def encontrar_caminho_recursivo(no, caminho_atual):
        if no is None:
            return None

        caminho_atual.append(no.valor)

        if no.valor == valor_alvo:
            return caminho_atual

        caminho_no_esquerda = encontrar_caminho_recursivo(no.esquerda, caminho_atual.copy())
        caminho_no_direita = encontrar_caminho_recursivo(no.direita, caminho_atual.copy())

        if caminho_no_esquerda:
            return caminho_no_esquerda
        if caminho_no_direita:
            return caminho_no_direita

        return None

    caminho = encontrar_caminho_recursivo(raiz, [])
    return caminho

raiz = TreeNode(1)
raiz.esquerda = TreeNode(2)
raiz.direita = TreeNode(3)
raiz.esquerda.esquerda = TreeNode(4)
raiz.esquerda.direita = TreeNode(5)
raiz.direita.esquerda = TreeNode(6)
raiz.direita.direita = TreeNode(7)

caminho_para_5 = encontrar_caminho(raiz, 5)
print(caminho_para_5)  
