class Livraria:
    def __init__(self, books):
        self.books = books
    
    def lista_livros(self):
        for book in self.books:
            print(book)

    def adicionar_livros(self, book):
        self.books.append(book)


class Livro:
    def __init__(self, nome):
        self.nome = nome

    
livro1 = Livro("Uma vida intelectual")
livro2 = Livro("Harry Potter")
livro3 = Livro("Senhor dos Aneis")

livros = [livro1.nome, livro2.nome, livro3.nome]

biblioteca = Livraria(livros)
biblioteca.adicionar_livros("guardiola a historia")
biblioteca.lista_livros()