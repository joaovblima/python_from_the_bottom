class Carrinho:
    def __init__(self, produtos):
        self.produtos = produtos


    def adiciona_produtos(self, produto):
        self.produtos.append(produto)
    
    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos(produto)

    def listar_produtos(self):
        if self.produtos == None:
            print("O carrinho está vazio")
        else:
            for produto in self.produtos:
                print(produto)