### Modulo 3 - Coleções

Coleções em Python são Estruturas de dados usados para armazenar grupos de dados. As mais comunns são:
    1. Listas: ordenadas, mutáveis(podem ser alteradas)
    2. Tuplas: ordenadas, imutáveis(não podem ser alteradas)
    3. Sets: desordenadas, não dúplicadas. 
    4. Dicionários: pares de key-value


#### 3.1 - Listas

Uma lista é como se fosse uma caixa onde você pode adicionar e mudar itens para o que você quiser. 

Exemplo:

```python

frutas = ["maça", "banana", "cereja"]

print(frutas[0]) #maça
print(frutas[-1]) #cereja

frutas.appende("manga") #adiciona item

frutas.remove("banana") #remove

print(frutas[1:3]) #slice

```


#### 3.2 - Tuplas

É como uma lista, porém não pode ser alterada

```python

cores = ("amarelo", "vermelho", "azul)
print(cores[0])
cores[1] = "rosa" #erro

```

#### 3.3 - Sets 

Set é uma coleção sem ordem e sem valores duplicados. útil para testes de associação 

Exemplos: 

```python

numeros = {1, 2, 3, 3, 4}

print(numeros)

numeros.add(5)
numeros.remove(2)

print(3 in numeros)


```

#### 3.4 - Dicionarios

Dicionarios armazena dados em pares de chaves:valor

Exemplo: 

```python

estudade = {
    "nome": "alice", 
    "idade": 21,
    "grade": "A"
}

print(estudante["nome"])
print(estudante["idade"])
print(estudante["idade"])
print(estudante)

for key, value in estudante.items():
    print(key,":", value)

```
