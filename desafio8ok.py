while True:
    try:
        num = int(input("\nInforme um número inteiro entre 1 e 10: "))
        if 1 <= num <= 10:
            break
        else:
            print("Valor informado inválido. Por favor, informe um número entre 1 e 10.")
    except ValueError:
        print("\nPor favor, digite um número inteiro.")
print("\nMostrando tabuada do {num}:")
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)