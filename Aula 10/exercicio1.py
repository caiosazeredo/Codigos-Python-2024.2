import random

numero1 = random.uniform(1, 15)
numero2 = random.uniform(1, 15)
numero3 = random.uniform(1, 15)

escolha = int(input("O sistema tem 3 numéros, qual dos 3 você acha que é o maior?"))

if escolha == 1 and numero1>numero2 and numero1>numero3:
    print("Você acertou! o primeiro numero era o maior")
elif escolha == 2 and numero2>numero1 and numero2>numero3:
    print("Você acertou! o segundo numero era o maior ")
elif escolha == 3 and numero3>numero1 and numero3>numero2:
    print("Você acertou! o terceiro numero era o maior ")
else:
    print("Você errou!")
print("os valores eram:")
print(numero1)
print(numero2)
print(numero3)