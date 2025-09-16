### Modulo 4 - Funções

Função é um bloco de código reutilizável que executa uma tarefa. Você pode definir uma função e depois chamá-la sempre que precisar.

Exemplo:

```python

def greet():
    print("ola boa noite")


greet()
```

#### 4.2 Funções com parâmetros

Funções que podem receber valores entrada (parâmetros)

```python

def greet(nome):
    print("olá", nome, "boa noite!")


greet("João")
```

### 4.3 Funções com retorno(return)

Funções podem devolver valores com return.

```python

def quadrado(x):
    return x * x

resultado = quadrado(4)
print(resultado)

```

### 4.4 Vários parâmetros

```python 

def add(a, b)
    return a + b


print(add(2, 5))

```
### 4.5 Argumentos nomeados (Keyword arguments)

```python

def introduce(nome, age):
    print("My name is", nome, "and I'm", age, "years old.")

introduce(nome="João", age=28)
```

### 4.6 Escopo de variáveis
Variáveis criadas dentro da função existem só lá dentro(escopo local)
Variáveis criadas fora da função são globais.

```python
x = 10

def minha_funcao():
    x = 5
    print("dentro da funcao", x)

minha_funcao()
print("fora da funcao", x)
```
### 4.7 Funções recursivas 

Uma função pode chamar a si mesma -> útil em alguns problemas

```python

def fatorial(n):
    if n ==0:
        return 1
    return n * fatorial(n-1)

print(fatorial(5))
```


