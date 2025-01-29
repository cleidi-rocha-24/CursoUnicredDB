user_ok="aluno"
senha_ok="segredo"
cont_tentativas = 0

while cont_tentativas <3:
    user = input("\nInforme o nome do usuário:")
    senha = input("Informe a senha:")

    if user ==user_ok and senha ==senha_ok:
        print("Bem vindo")
        break
    else:
        print("\nFalha ao realizar o login! Faça nova tentativa.")
        cont_tentativas +=1

        if cont_tentativas ==3:
            print("\nAcesso bloqueado! Tentativas de login ultrapassaram 3 tentativas")