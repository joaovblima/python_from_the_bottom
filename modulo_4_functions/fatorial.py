def fatorial(numero):
    contador = numero
    soma =1
    while contador >=1:
        soma *=contador
        contador-=1
    return soma

print(fatorial(6))