#Trocando valores entre as variaveis
numero1 = 5
numero2 = 8
numero3 = 10
numero4 = 20
if numero2 > numero1:
    #Variavel auxiliar recebe o numero 2
    auxiliar = numero2
    #Numero2 recebe o numero 1
    numero2 = numero1
    #numero1 recebe a variavel auxiliar
    numero1 = auxiliar
    print(numero1)
    print(numero2)
#troca simultânea de valores
numero3, numero4 = numero4, numero3
print(numero3)
print(numero4)