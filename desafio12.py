
numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

impares = []

for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)

print(f"\nA quantidade de valores ímpares no vetor é: {len(impares)}")
print("Os números ímpares informados são:\n", impares)