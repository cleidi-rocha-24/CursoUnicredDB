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
    { "id": 10, "nome": "Papel Higiênico", "quantidade": 80, "preco": 12.00 }
]
'''

class Mercado:
    def __init__(self):
        self.produtos = json.loads(produto_json)

    def adicionar_produtos(self, nome_produto, quantidade, preco): 
        produto = {             
            'nome': nome_produto,             
            'quantidade': quantidade,             
            'preco': preco 
        } 
        self.produtos.append(produto) 
       
    def exibir_lista_produtos(self):
       for produto in self.produtos:
            nome = produto["nome"]
            quantidade = produto["quantidade"]
            preco = produto["preco"]
                      
            print(f'Produto: {nome}, Quantidade: {quantidade}, Preço Unitário: R${preco:.2f}')
                 
    def valor_e_quantidade_total_produto(self):
        quantidade_total = 0
        valor_total_produto = 0
        for produto in self.produtos:
            quantidade_total += produto["quantidade"]       
            valor_total_produto += produto["quantidade"] * produto["preco"]
            #valor_total = valor_total + valor_total_produto 
        print(f'Quantidade total dos produtos no mercado:{quantidade_total}')
        print(f'Valor total dos produtos no mercado: R${valor_total_produto:.2f}')

    
produto = Mercado()
produto.adicionar_produtos("nome_produto_tst",2,2.50) #ajustar para possibilitar que usuário digite
produto.exibir_lista_produtos()
produto.valor_e_quantidade_total_produto()


    
   
