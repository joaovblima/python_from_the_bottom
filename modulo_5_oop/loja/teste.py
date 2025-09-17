from produto import Produto
from carrinho_de_compras import Carrinho


suco = Produto("Suco de Laranja", 3.50)
coca = Produto("Coca-Cola", 12)

produtos = [suco, coca]

carrinho = Carrinho(produtos)
carrinho.listar_produtos()