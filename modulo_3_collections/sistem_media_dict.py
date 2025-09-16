alunos = {
    "João": [7, 8, 9],
    "Maria": [10, 9, 8],
    "Pedro": [5, 6, 7]
}

aluno_media = {}

for k, v in alunos.items():
    aluno_media[k] = sum(v) / len(v)

print(aluno_media)

maior = max(aluno_media.values())
for chave, valor in aluno_media.items():
    if valor == maior:
        print("a maior média é de",chave.title())