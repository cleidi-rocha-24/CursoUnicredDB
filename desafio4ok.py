#retorna validação apos digitado algum caracter errado
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except(Exception):
    raise Exception("valor informado errado")


print("Informe a operação a ser calculada:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Informe o número referente à operação desejada: ")

match operacao:
        case "1":
            result = num1 + num2
            print(f"Resultado da adição é: {result:.2f}")
        case "2":
            result = num1 - num2
            print(f"Resultado da subtração é: {result:.2f}")
        case "3":
            result = num1 * num2
            print(f"Resultado da multiplicação é: {result:.2f}")
        case "4":
            if num2 != 0:
                result = num1 / num2
                print(f"Resultado da divisão é: {result:.2f}")
            else:
                print("Divisão por zero é inválida.")
        case _:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")