class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        
class Mercado:
    def __init__(self):
        self.produto = []

    def adicionar_produtos(self, itens_adicionado): 
        self.produto.append(itens_adicionado) 
       
    def exibir_lista_produtos(self):
       for produtos in self.produto:
            id = produtos.id
            nome = produtos.nome
            quantidade = produtos.quantidade
            preco = produtos.preco
                      
            print(f'ID: {id}, Produto: {nome}, Quantidade: {quantidade}, Preço Unitário: R${preco:.2f}')
                 
    def valor_e_quantidade_total_produto(self):
        quantidade_total = 0
        valor_total_produto = 0
        for produtos in self.produto:
            quantidade_total += produtos.quantidade       
            valor_total_produto += produtos.quantidade * produtos.preco
        print(f'Quantidade total dos produtos no mercado:{quantidade_total}')
        print(f'Valor total dos produtos no mercado: R${valor_total_produto:.2f}')

import json
produto_json = '''
[
    { "id": 1, "nome": "Arroz", "quantidade": 50, "preco": 20.99 },
    { "id": 2, "nome": "Feijão", "quantidade": 30, "preco": 8.50 },
    { "id": 3, "nome": "Macarrão", "quantidade": 40, "preco": 5.90 },
    { "id": 4, "nome": "Açúcar", "quantidade": 25, "preco": 4.20 },
    { "id": 5, "nome": "Café", "quantidade": 60, "preco": 14.70 },
    { "id": 6, "nome": "Leite", "quantidade": 100, "preco": 4.80 },
    { "id": 7, "nome": "Óleo de Soja", "quantidade": 70, "preco": 9.50 },
    { "id": 8, "nome": "Sabonete", "quantidade": 200, "preco": 1.50 },
    { "id": 9, "nome": "Detergente", "quantidade": 150, "preco": 2.30 },
    { "id": 10, "nome": "Papel Higiênico", "quantidade": 90, "preco": 22.00 }
]
'''
produtosArquivo = json.loads(produto_json)
mercado = Mercado()
for item in produtosArquivo:
    idProduto = item["id"]
    nomeProduto = item["nome"]
    quantProduto = item ["quantidade"]
    precoProduto = item ["preco"]
    
    produto = Produto(idProduto,nomeProduto,quantProduto,precoProduto)
    mercado.adicionar_produtos(produto)

mercado.exibir_lista_produtos()
mercado.valor_e_quantidade_total_produto()


    
   
