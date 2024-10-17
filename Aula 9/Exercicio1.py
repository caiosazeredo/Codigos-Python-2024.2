jogar = True
while jogar == True:
    contador = 0
    print("Kahoot Iniciado")
    resposta1 = input(("Int significa inteiro? s/n:")).lower()
    if(resposta1 == "s"):
        print("Acertou")
        contador += 1
    else:
        print("Errou")
        print("A traducação de int é inteiro, ou seja, uma variavel com esse atributo recebera apenas numeros inteiros")
    resposta2 = input(("float significa numero diferente? s/n:")).lower()
    if(resposta2 == "n"):
        print("Acertou")
        contador += 1
    else:
        print("Errou")
        print("Float significa Ponto Flutuante")
    resposta3 = input(("print significa imprimir? s/n:")).lower()
    if(resposta3 == "s"):
        print("Acertou")
        contador += 1
    else:
        print("Errou")
        print("Print é imprimir, ou seja, aparecer alguma informação na tela")            
    Quantidade_de_perguntas = 3
    if(contador/2 >= Quantidade_de_perguntas/2):
        print("Parabens, você venceu")
    else:
        print("Não foi dessa vez!")
    perguntar = input("Deseja jogar novamente?s/n:")
    if(perguntar == "n"):
        jogar=False