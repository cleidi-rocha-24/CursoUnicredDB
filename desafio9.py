num1 = float(input("\nDigite um número inteiro a ser dividido: "))

while True:
    divisor = float(input("\nDigite o divisor que seja diferente de zero: "))
    if divisor != 0:
        break
    else:
        print("\nInsira um valor diferente de zero!")

# divisão
resultado = num1 // divisor

print(f"O resultado da divisão de {num1} por {divisor} é: {resultado}")

