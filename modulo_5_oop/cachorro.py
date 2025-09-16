class Animal:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        print("aLGUMA COISA")
        
class Cachorro(Animal):

    def falar(self):
        print(self.nome, "diz: woof woof")


cachorro1 = Cachorro("Zé alfredo")
cachorro2 = Cachorro("mEL")

cachorro1.falar()
cachorro2.falar()