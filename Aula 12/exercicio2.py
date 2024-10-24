matriz2 = [
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""],
    ["", "", "", "", ""]
]
matriz1 = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]
armario = input("Qual armario você gostaria de adquirir vip ou normal?").lower()
nome = input("Qual o seu nome?")

if armario == "vip":
    linha = int(input("Em qual linha do armário será a sua gaveta? (0 a 2)"))
    coluna = int(input("Em qual coluna do armário será a sua gaveta? (0 a 2)"))
    matriz1[linha][coluna] = nome
    print("O preço será R$50,00")
    for linha in matriz1:
        print(linha)
elif armario == "normal":
    linha = int(input("Em qual linha do armário será a sua gaveta? (0 a 4)"))
    coluna = int(input("Em qual coluna do armário será a sua gaveta? (0 a 4)"))
    matriz2[linha][coluna] = nome
    print("O preço será R$30,00")
    for linha in matriz2:
        print(linha)
else:
    print("armario não identificado")



