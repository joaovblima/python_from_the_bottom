caixa = {
    "coca-cola": 10,
    "brigadeiro gourmet": 9, 
    "pipoca": 8, 
    "cigarro": 4, 
    "ketchup": 2
}

texto = """
Bem-vindos ao nosso caixa aqui vão as opções:

1 - Adicionar um produto: 
2 - Vender um produto: 
3 - Mostrar todos os produtos: 
"""

print(texto)
opcao = input()

if opcao == "1":
    produto = input("Nome produto: ")
    if produto in caixa:
        caixa[produto] +=1
    print(caixa)
elif opcao == "2":
    produto = input("Qual produto você quer vender: ")
    caixa[produto] -=1
    print(caixa)
elif opcao == "3":
    for k, v in caixa.items():
        print(k.title(),".",  "Quantidade: ", v)