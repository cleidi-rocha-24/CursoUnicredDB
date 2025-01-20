
def main():
    
    nota1 = input("Digite a primeira nota do aluno: ")
    nota2 = input("Digite a segunda nota do aluno: ")
    nota3 = input("Digite a terceira nota do aluno: ")

    if nota1.replace('.', '', 1) and nota2.replace('.', '', 1) and nota3.replace('.', '', 1):
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)

        # Calculando a média
        media = (nota1 + nota2 + nota3) / 3

        # Determinando o resultado
        if media >= 7:
            print(f"Média: {media:.2f} - Aprovado")
        elif media >= 5:
            print(f"Média: {media:.2f} - Recuperação")
        elif media < 5:
            print(f"Média: {media:.2f} - Reprovado")
   

if __name__ == "__main__":
    main()
