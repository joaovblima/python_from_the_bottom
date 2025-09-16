# Modulo 1: Python Básico

### Topicos 
    1. Printando e Comentários
    2. Variáveis e Tipos de dados(int, float, str, bool)
    3. Input direto do usuário
    4. Aritmética Básica


#### Printando e Comentários

Para mostar algo na tela, no nosso terminal temos que utilizar uma função chamada print(), vamos ver como ela funciona na prática: 

```python

print("Olá mundo")
```

Comentários são muito úteis se quisermos explicar alguma parte de nosso código

```python

#esse é um comentário, nada que está escrito aqui é mostrado no programa.
```

#### Variáveis e tipos de dados

Criamos variáveis para utilizarmos posteriormente no código, usamos o padrão snake_case,
é importante respeitar os padrões utilizados pela comunidade.

```python
nome = "joao"
```
No python possuimos alguns tipos de dados são eles: int que são números inteiros, float que são números decimais, str que são as strings e bool os booleanos(true e false);

#### Input direto do usuário

Se quisermos receber dados digitados do usuário utilizamos a função input, todo dado recebido de input é uma string, se você quiser fazer operações como somar números entre outras, é necessário a conversão de tipo para o tipo desejado.

```python
nome = input("Qual é o seu nome? ")

```
Se quisermos receber números do usuário para realizar somas podemos converter 

```python
num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundoo numero: "))

```



