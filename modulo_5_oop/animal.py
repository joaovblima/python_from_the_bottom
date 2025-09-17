class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print(self.nome, "fale fale fale")

class Cachorro(Animal):
    
    def falar(self):
        print("au au au canta", self.nome)

class Gato(Animal):

    def falar(self):
        print("miau miau miau rorona", self.nome)


mel = Cachorro("Mel")
mel.falar()
piru = Gato("Pirulit")
piru.falar()