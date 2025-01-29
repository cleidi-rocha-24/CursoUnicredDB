""" nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print('Media: ',media)
if media<7.0:
    print('Reprovado')
elif media<10:
    print('Aprovado') """


def calculo_media():
    # Solicita as duas notas ao usuário
    nota1 = float(input("\nDigite a primeira nota em número inteiro: "))
    nota2 = float(input("Digite a segunda nota em número inteiro:: "))

    media = (nota1 + nota2) / 2

    print(f"\nA média final para as notas informadas: {nota1} e {nota2} Foi: {media:.2f}")

    if media >= 7:
        print("\nAluno foi aprovado!")
    else:
        print("\nAluno foi reprovado!")

while True:
    calculo_media()
    resposta = input("\nDeseja realizar um novo cálculo? (S/N): ").lower()
    if resposta != 's':
        print("Programa encerrado.")
        break