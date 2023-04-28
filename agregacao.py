class Carrinho:
    def __init__(self) -> None:
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def listar_produtos(self):
        print()
        for produtos in self._produtos:
            print(produtos.nome, produtos.preco)

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)


class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1,p2)
carrinho.listar_produtos()
print(carrinho.total())