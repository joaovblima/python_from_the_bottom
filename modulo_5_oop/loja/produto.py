class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    
    def __str__(self):
        return f"{self.nome}, preço: R${self.preco:.2f}"