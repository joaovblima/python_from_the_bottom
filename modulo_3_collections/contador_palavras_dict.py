frase = input("Diga qual a frase: ")

#usei split para formar uma lista de palavras
palavras = frase.split(" ")

#criei um dicionario vazio 
frequencia = {}
#percorri a lista de palavras usando a keyword "palavra" para percorrer a lista de palavras
for palavra in palavras:
    #coloquei todas as palaras no lowercase
    palavra = palavra.lower()
    #se a palavra está em sequencia eu adiciono +1 na contagem
    if palavra in frequencia:
        frequencia[palavra] +=1
    #se não estiver eu adiciono ela    
    else:
        frequencia[palavra] = 1

#percorro o dicionario
for k, w in frequencia.items():
    print(k, ": ", w)