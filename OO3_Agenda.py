class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class AgendaTelefonica:
    def __init__(self): 
        self.agenda = []

    def validarExistenciaDeContato(self, nome:str):
        nome = nome.lower()
        for contato in self.agenda:
            if contato.nome.lower() == nome:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
                return contato
        return None
         
    def buscarContato(self,nome:str):
        contato = self.validarExistenciaDeContato(nome)
        if contato:
            return contato
              

    def adicionarContato(self,contato:Contato):
        if self.validarExistenciaDeContato(contato.nome) is None:
            self.agenda.append(contato)
            print("\nContato adicionado com sucesso")
        else:
            print("\nRegistro já existente! informe novo nome")


    def removerContato(self,nome:str):
        contato = self.validarExistenciaDeContato(nome)
        if contato:
            self.agenda.remove(contato)
            print("\nContato removido com sucesso.")
        
    def atualizarContato(self,nome:str,contato_editado:Contato):
        contato = self.buscarContato(nome)
        if contato:
            contato.nome = contato_editado.nome
            contato.telefone = contato_editado.telefone
            print("\nContato atualizado com sucesso.")
    
    def listarContatos(self):
        if not self.agenda:
            print("\nNão possui registros na agenda.")
        else:
            print("\nAgenda\n------")
            for contato in self.agenda:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
            print("------\n")


class Menu(AgendaTelefonica):
    def menu(self):
        while True: 
            print("""
                1 - Adicionar novo contato
                2 - Remover um contato existente.
                3 - Buscar um contato
                4 - Atualizar informações de um contato
                5 - Listar todos os contatos
                6 - Sair
            """)
            opcao = self.validar("Escolha uma opção: ",1,6) 

                                
            if opcao == 6:
                print("\nVocê esta saindo..")                     
                break
            elif opcao == 1:
                nome = input ("Informe o nome:")
                telefone = input ("Informe o telefone:")
                contato = Contato(nome,telefone)
                super().adicionarContato(contato)
            elif opcao == 2:
                nome_exclusao = input ("Informe nome a ser excluído:")
                super().removerContato(nome_exclusao)
            elif opcao == 3:
                nome_busca = input ("Informe nome a ser localizado:")
                super().buscarContato(nome_busca)
            elif opcao == 4:
                nome_edicao = input ("Informe o nome a ser buscado para alteração: ")
                nome_alterado = input ("Informe o nome a ser alterado: ")
                telefone_edicao = input ("Informe o telefone a ser alterado: ")
                contato_editado = Contato(nome_alterado,telefone_edicao)
                super().atualizarContato(nome_edicao,contato_editado)
            elif opcao == 5:
                super().listarContatos()

    def validar(self,valor_entrada,inicio, fim):          
        while True:                            
            try:                                
                valor = int(input(valor_entrada))  
                if inicio <= valor <= fim:   
                    return(valor)             
                return                        
            except (ValueError,TypeError):                 
                print(f"\nValor inválido, favor digitar entre {inicio} e {fim}")
            except KeyboardInterrupt:
                print("\nO usuário optou por não informar os dados") 
                break

menu = Menu()
menu.menu()

