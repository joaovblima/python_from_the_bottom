### Modulo 5 - Programação Orientada a Objetos

A programação orientada a objetos é um jeito de organizar o código usando classes e objetos. 
É muito usada em Python(e praticamente toda linguagem moderna).

#### 5.1 Classes e Objetos

Classe -> um molde, como uma planta de uma casa
Objeto -> Uma instância de classe, como uma casa construida a partir de uma planta.

Exemplo: 

```python 
Class Dog:
    def __self__(self, name):
        self.name = name

    def latido(self):
        print(self.name, "says:  woof")

dog1 = Dog("Rex")
dog2 = Dog("Luna")

dog1.latido()
dog2.latido()
```

### 5.2 O Método __init__
É o construtor da classe. Ele roda toda vez que vocÊ cria um objeto.

```python

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def introducao(self):
        print("Olá, meu nome é", self.nome, "eu tenho", self.idade, "anos de idade")

```

### 5.3 Atributos e métodos

Atributos -> variáveis de classe(nome, idade)
Métodos -> funções dentro da classe(ex: introducao())

### 5.4 Herança

Uma classe pode herdar caracteristicas da outra

```python 
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falat(self):
        print("apodadkçlq")


class Gato(Animal):
    def speak(self):
        print(self.nome, "fala: meowww")
```

### 5.5 Encapsulamento

Python não tem privacidade rigida igual C# E JAVA, MAS A CONVENÇÃO É:

self.name -> publico
_self.name -> protegido
__self.name -> privado(python aplica name mangling)