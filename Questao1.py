class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

raiz = No(10)
no_esquerdo = No(5)
no_direito = No(15)
raiz.no_esquerdo = no_esquerdo
raiz.no_direito = no_direito
