# Inicializa uma lista vazia para armazenar os nomes
lista = []

# Solicita ao usuário que insira 10 nomes
for i in range(10):
    dado = input(f"Digite o {i+1}º nome: ")
    lista.append(dado)

# Solicita ao usuário que insira um nome para verificação
novo_nome= input("\nInforme novo nome para verificar se já está na lista: ")

# Verifica se o nome está na lista
if novo_nome in lista:
    print("\nAchei")
else:
    print("\nNão achei")