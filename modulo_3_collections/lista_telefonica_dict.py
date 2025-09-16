lista_telefonica = {
    "joao": "9999-9999", 
    "leticia": "8888-8888", 
    "ingrid": "3333-3333", 
    "maria sofia": "4444-4444"
}

pessoa = input("Qual pessoa você quer saber o numero: ")

if pessoa in lista_telefonica:
    print(lista_telefonica[pessoa])
else:
    print("a pessoa não está na lista")