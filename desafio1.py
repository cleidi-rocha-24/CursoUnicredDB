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

# Carrega os dados do JSON
produtos = json.loads(produto_json)


valor_tot = 0

# loop sobre os produtos e mostra informações
for produto in produtos:
    nome = produto["nome"]
    quantidade = produto["quantidade"]
    preco = produto["preco"]
    valor_tot_prod = quantidade * preco
    valor_tot = valor_tot + valor_tot_prod
    
    # mostra informaçoes dos produtos
    print(f'Produto: {nome}, Quantidade: {quantidade}, Preço Unitário: R${preco:.2f}, Valor Total: R${valor_tot_prod:.2f}')

# mostra valor total dos produtos
print(f'Valor total dos produtos no mercado: R${valor_tot:.2f}')