class Livro:
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    
    livro=[]

    def buscarLivro(self,titulo:str):
        titulo = titulo.lower()
        for busca_livros in self.livro:
            if busca_livros.titulo.lower() == titulo:
                return busca_livros
        return None
    
    def adicionarLivro(self,informacoes_livro:Livro):
        if self.buscarLivro(informacoes_livro.titulo) is None:
            self.livro.append((informacoes_livro))
            print(f"\nLivro {informacoes_livro.titulo} do autor {informacoes_livro.autor} adicionado com sucesso")
        else:
            print(f"\nLivro {informacoes_livro.titulo} do autor {informacoes_livro.autor} já existente! informe novo livro")

    def listarLivros(self):
        if not self.livro:
            print("\nNão possui registros na biblioteca.")
        else:
            print("\nListando livros existentes:\n------")
            for livros in self.livro:
                print(f"Título: {livros.titulo}, Autor: {livros.autor}")
            print("------\n")

    def emprestarLivros(self,titulo:str):
        self.buscarLivro(titulo)
        for busca_disponiveis in self.livro:
            if titulo == busca_disponiveis.titulo and busca_disponiveis.disponivel == True:
                busca_disponiveis.disponivel = False
                print(f"Livro {busca_disponiveis.titulo} emprestado com sucesso")
                break
            elif titulo == busca_disponiveis.titulo and busca_disponiveis.disponivel == False:
                print(f"\nLivro {busca_disponiveis.titulo} não esta disponível para emprestimo")

    def devolverLivros(self,titulo:str):
        self.buscarLivro(titulo)
        for livros_emprestados in self.livro:
            if titulo == livros_emprestados.titulo and livros_emprestados.disponivel == False:
                livros_emprestados.disponivel = True
                print(f"\nLivro {livros_emprestados.titulo} devolvido com sucesso")
                break
            elif titulo == livros_emprestados.titulo and livros_emprestados.disponivel == True:
                print(f"\nLivro {livros_emprestados.titulo} não consta como emprestado")

def main():
        
    biblioteca = Biblioteca()

    # Adicionando livros
    livro1 = Livro("Pequeno Príncipe", "Autor do Pequeno principe")
    livro2 = Livro("Harry Potter", "Autor do Harry")
    try:
        biblioteca.adicionarLivro(livro1)
        biblioteca.adicionarLivro(livro2)
    except TypeError:
        print("\nDado informado é inválido!")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    try:  
        biblioteca.listarLivros()
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    try:  
    # Emprestando um livro
        biblioteca.emprestarLivros("Harry Potter")
    # Emprestando livro já emprestado
        biblioteca.emprestarLivros("Harry Potter")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")  

    try:   
    # Devolvendo um livro
        biblioteca.devolverLivros("Pequeno Príncipe") #não emprestado
        biblioteca.devolverLivros("Harry Potter") #já emprestado
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}") 

    try: 
    # Tentativa de adicionar um livro duplicado
        livro3 = Livro("Pequeno Príncipe", "Autor do Pequeno principe")
        biblioteca.adicionarLivro(livro3)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

 
if __name__ == "__main__":
    main()
        

