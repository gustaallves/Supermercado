from My_library.some_module import Colaborador, Cliente, Produto, Venda

def workspace():
    # Criar alguns colaboradores
    colaborador1 = Colaborador('João', '1234', 30, 'Caixa')

    # Criar um cliente
    cliente1 = Cliente('José')
    

    # Criar alguns produtos
    produto1 = Produto('Arroz', 'Alimento', 10.50)
    produto2 = Produto('Feijão', 'Alimento', 8.99)
    produto3 = Produto('Sabão em Pó', 'Limpeza', 5.50)
    
    # Criar uma venda
    venda1 = Venda(cliente1, colaborador1)
    
    # Adicionar produtos à venda
    venda1.adicionar_produto(produto1)
    venda1.adicionar_produto(produto2)
    venda1.adicionar_produto(produto3)
    
    # Finalizar a venda
    venda1.finalizar_venda()

    
        
    print("\nSuccessful exit.")
    
    
    
if __name__ == "__main__":
    
    workspace()

