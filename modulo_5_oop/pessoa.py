class Pessoa:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade = idade

    def intro(self):
        print("Olá, meu nome é", self.nome, "e eu tenho", self.idade, "anos de idade.")


p1 = Pessoa("João", 28)
p1.intro()