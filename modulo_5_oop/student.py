class Estudantes:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def media(self):
        soma = 0
        media = 0
        for notas in self.notas:
            soma += notas
            media = soma / len(self.notas)
        print(f"A média de notaas é {media}")


joao = Estudantes("joao", [10, 8, 7, 3, 5])
joao.media()
