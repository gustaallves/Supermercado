class Entidade:
    def __init__(self, nome):
        self.nome = nome

class Colaborador(Entidade):
    def __init__(self, nome, matricula, idade, funcao):
        super().__init__(nome)
        self.matricula = matricula
        self.idade = idade
        self.funcao = funcao

    def mostrar_colaborador(self):
        """Informações sobre o Colaborador"""
        print(f'Nome do colaborador: {self.nome}\nMatrícula: {self.matricula}\nIdade: {self.idade}\nFunção: {self.funcao}')

class Cliente(Entidade):
    def __init__(self, nome):
        super().__init__(nome)

    def mostrar_cliente(self):
        """Nome do Cliente"""
        print(f'Nome do Cliente: {self.nome.title()}')

class Produto(Entidade):
    def __init__(self, nome, categoria, preco):
        super().__init__(nome)
        self.categoria = categoria
        self.preco = preco

    def mostrar_produto(self):
        """Informações sobre o produto"""
        print(f'Nome do Produto: {self.nome}\nCategoria: {self.categoria}\nPreço: R$ {self.preco:.2f}')

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        """Adiciona um produto ao carrinho"""
        self.produtos.append(produto)

    def remover_produto(self, produto):
        """Remove um produto do carrinho"""
        if produto in self.produtos:
            self.produtos.remove(produto)
        else:
            print('Produto não encontrado no carrinho.')

    def calcular_total(self):
        """Calcula o valor total dos produtos no carrinho"""
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

class Venda:
    def __init__(self, cliente, colaborador):
        self.cliente = cliente
        self.colaborador = colaborador
        self.carrinho = CarrinhoDeCompras()

    def adicionar_produto(self, produto):
        """Adiciona um produto à venda"""
        self.carrinho.adicionar_produto(produto)

    def remover_produto(self, produto):
        """Remove um produto da venda"""
        self.carrinho.remover_produto(produto)

    def calcular_total(self):
        """Calcula o valor total da venda"""
        return self.carrinho.calcular_total()

    def finalizar_venda(self):
        """Finaliza a venda e imprime o recibo"""
        print('-' * 40)
        print('               SUPERMERCADO UNB               ')
        print('-' * 40)
        print('Cliente:', self.cliente.nome)
        print('Colaborador:', self.colaborador.nome)
        print('-' * 40)
        for produto in self.carrinho.produtos:
            print(produto.nome, '-', f'R$ {produto.preco:.2f}')
        print('-' * 40)
        print('Total: R$', f'{self.calcular_total():.2f}')
        print('-' * 40)
        



    