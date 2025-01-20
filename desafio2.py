#
# Primeiro produto
nome1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input(f"Digite o preço de '{nome1}': R$"))
quantidade1 = int(input(f"Digite a quantidade de '{nome1}': "))

# Segundo produto
nome2 = input("Digite o nome do segundo produto: ")
preco2 = float(input(f"Digite o preço de '{nome2}': R$"))
quantidade2 = int(input(f"Digite a quantidade de '{nome2}': "))

# Terceiro produto
nome3 = input("Digite o nome do terceiro produto: ")
preco3 = float(input(f"Digite o preço de '{nome3}': R$"))
quantidade3 = int(input(f"Digite a quantidade de '{nome3}': "))

# Quarto produto
nome4 = input("Digite o nome do quarto produto: ")
preco4 = float(input(f"Digite o preço de '{nome4}': R$"))
quantidade4 = int(input(f"Digite a quantidade de '{nome4}': "))

# Cálculo do total sem desconto
quantidade_total = quantidade1 + quantidade2 + quantidade3 + quantidade4
valor_total = (preco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3) + (preco4 * quantidade4)

# Aplicação do desconto f
if quantidade_total <= 10:
    desconto = 0
elif quantidade_total <= 20:
    desconto = 0.10
elif quantidade_total <= 50:
    desconto = 0.20
elif quantidade_total > 50:
    desconto = 0.25

# Cálculo do valor final com desconto
valor_com_desconto = valor_total * (1 - desconto)

# Exibição do resumo
print("\n--- Resumo da Compra ---")
print(f"Produto: {nome1}, Preço Unitário: R${preco1:.2f}, Quantidade: {quantidade1}, Subtotal: R${preco1 * quantidade1:.2f}")
print(f"Produto: {nome2}, Preço Unitário: R${preco2:.2f}, Quantidade: {quantidade2}, Subtotal: R${preco2 * quantidade2:.2f}")
print(f"Produto: {nome3}, Preço Unitário: R${preco3:.2f}, Quantidade: {quantidade3}, Subtotal: R${preco3 * quantidade3:.2f}")
print(f"Produto: {nome4}, Preço Unitário: R${preco4:.2f}, Quantidade: {quantidade4}, Subtotal: R${preco4 * quantidade4:.2f}")

print(f"Total de itens: {quantidade_total}")
print(f"Valor total (sem desconto): R${valor_total:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor final (com desconto): R${valor_com_desconto:.2f}")