from csv import reader


class CaixaDoAtacado:

    def cardapio(self,id_produto):
        match id_produto:
            case 1:
                preco_prod = 53.00
                nome_prod = "Café 1kg"
            case 2:
                preco_prod = 36.00
                nome_prod = "Sabão em pó"
            case 3:
                preco_prod = 82.00
                nome_prod = "Caixa de Leite"
            case 4:
                preco_prod = 8.50
                nome_prod = "Refrigerante"
        return preco_prod,nome_prod
    
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
            preco_produto,nome_produto = self.cardapio(id_produto) 
            valor_total_desconto_item = (preco_produto-(desconto_item*preco_produto))*qtde_item
            total += valor_total_desconto_item
            print(f"\nproduto:{nome_produto}, quantidade:{qtde_item}, preço produto:{preco_produto:.2f}, total item com desconto:{valor_total_desconto_item:.2f}")
                    
        if metodo_pagamento == "Credito":
            total = total + (desconto_forma_pag*total)
        else:
            total = total - (desconto_forma_pag*total)
        print(f"\nTotal aplicando calculo forma de pagamento:{total:.2f}")
        return total
               
    def percentual_desconto(self,quantidade_total):
        if quantidade_total <= 10:
            return 0
        elif quantidade_total <= 20:
            return 0.10
        elif quantidade_total <= 50:
            return  0.20
        else: 
            quantidade_total > 50
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


            

            