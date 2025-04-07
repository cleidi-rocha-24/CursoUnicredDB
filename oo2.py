from csv import reader

class Produto:
    def __init__(self,id,nome,preco):
        self.id = id
        self.nome = nome
        self.preco = preco

class CaixaDoAtacado:
    cardapio = {
        1: Produto(1, "cafe 1kg", 53.00),
        2: Produto(2, "Sabão em Pó", 36.00),
        3: Produto(3, "Caixa de Leite", 82.00),
        4: Produto(4, "Refrigerante", 8.50),
    }

    def ler_arquivo_csv(self,nome_arquivo):
        with open(nome_arquivo) as arquivo:
            arquivo_lido = reader(arquivo)
            lista_id_qtde = []
            metodo_pagamento = next(arquivo_lido)[0]
            for i in arquivo_lido:
                id_item = int(i[0])
                qtde = int(i[1])
                lista_id_qtde.append((id_item,qtde))
        return metodo_pagamento,lista_id_qtde
    
    def computar_compra(self,arquivo):
        metodo_pagamento, lista_id_qtde = self.ler_arquivo_csv(arquivo)
        total = 0
        desconto_forma_pag = self.desconto_metodo_pagamento(metodo_pagamento) 
        for id_produto, qtde_item in lista_id_qtde:
            desconto_item = self.percentual_desconto(qtde_item) 
            prod_dicionario = self.cardapio[id_produto]
            prod_preco = prod_dicionario.preco
            prod_nome = prod_dicionario.nome
            valor_total_desconto_item = (prod_preco-(desconto_item*prod_preco))*qtde_item
            total += valor_total_desconto_item
            print(f"\nproduto:{prod_nome}, quantidade:{qtde_item}, preço produto:{prod_preco:.2f}, total item com desconto:{valor_total_desconto_item:.2f}")
                    
        if metodo_pagamento == "Credito":
            total = total + (desconto_forma_pag*total)
        else:
            total = total - (desconto_forma_pag*total)
        print(f"\nTotal aplicando calculo sobre forma de pagamento:{total:.2f}")
        return total
               
    def percentual_desconto(self,quantidade_total):
        if quantidade_total <= 5:
            return 0
        elif quantidade_total <= 15:
            return 0.10
        elif quantidade_total <= 25:
            return  0.20
        else: 
            quantidade_total > 25
            return 0.25 

    def desconto_metodo_pagamento(self,forma_pagamento):
        match forma_pagamento:
            case "Debito": 
                return 0
            case "Dinheiro":
                return 0.05
            case "Credito":
                return 0.03 
            
   
caixa = CaixaDoAtacado()
caixa.computar_compra("compra.csv")


            

            