def maior_menor(lista):
    maior, menor = max(lista), min(lista)
    return maior, menor

lista_numeros = [10, 20, 432, 112]

resultado = maior_menor(lista_numeros)
print("maior: ", resultado[0], ", menor: ", resultado[1])