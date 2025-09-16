def palindromo(palavra):
    palavra = palavra.lower().replace(" ", " ")

    return palavra == palavra[::-1]

print(palindromo("arara"))