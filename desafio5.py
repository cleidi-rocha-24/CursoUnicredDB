nome_corretor = input("Informe o nome do corretor que vendeu imóvel: ")
valor_imovel = float(input("Informe o valor do imóvel vendido: "))

meta1 = 50000
meta2 = 30000

if valor_imovel >= meta1:
    print("\nCorretor bateu meta de vendas!!!!!!!!!!!!!")
    comissao = valor_imovel * 0.20 
    print(f"Nome do corretor:{nome_corretor}, Valor do imóvel: R${valor_imovel:.2f}, Comissão do corretor: R${comissao:.2f}\n")
elif valor_imovel >=meta2:
    print("\nCorretor bateu meta de vendas!!!!!!!!!!!!!")
    comissao = valor_imovel * 0.15 
    print(f"Nome do corretor:{nome_corretor}, Valor do imóvel: R${valor_imovel:.2f}, Comissão do corretor: R${comissao:.2f}\n")
else: 
    valor_imovel <meta2
    print("\nCorretor bateu meta de vendas!!!!!!!!!!!!!")
    comissao = valor_imovel * 0.10 
    print(f"Nome do corretor:{nome_corretor}, Valor do imóvel: R${valor_imovel:.2f}, Comissão do corretor: R${comissao:.2f}\n")




        