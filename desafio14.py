lista = []

for i in range(20):
    nome = input(f"Informe o {i+1}º nome: ")
    lista.append(nome)

lista_unicos = list(dict.fromkeys(lista))

print("\nLista dos nomes após a remoção dos duplicados:")
for nome in lista_unicos:
    print(nome)