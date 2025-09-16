lista_numeros = []

for i in range(5):
    numero = int(input("Digite um numero: "))
    lista_numeros.append(numero)

print("Maior é: ", max(lista_numeros))
print("Menor é:", min(lista_numeros))


def encontrar_maior_menor(lista):
    if not lista:
        return None, None
    
    maior= menor = lista[0]

    for num in lista:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    return maior, menor



lista = [10, 20, 3, 5]
maior, menor = encontrar_maior_menor(lista)
print("maior é", maior)
print("menor é", menor)