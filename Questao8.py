class No:
    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None

def travessia_em_niveis(raiz):
    if raiz is None:
        return []

    valores = []
    fila = [raiz]

    while fila:
        no_atual = fila.pop(0)
        valores.append(no_atual.valor)

        if no_atual.no_esquerdo:
            fila.append(no_atual.no_esquerdo)
        if no_atual.no_direito:
            fila.append(no_atual.no_direito)

    return valores

raiz = No(10)
raiz.no_esquerdo = No(5)
raiz.no_direito = No(15)
raiz.no_esquerdo.no_esquerdo = No(3)
raiz.no_esquerdo.no_direito = No(7)

valores_em_niveis = travessia_em_niveis(raiz)
print("Travessia em níveis:", valores_em_niveis) 
