import random

print("Você gostaria de adivinhar 1 ou 2 números simultaneamente?")
quantidade_numeros = int(input("Escolha a quantidade de números (1 ou 2): "))

# Inicializa os números e o status de acerto
if quantidade_numeros >= 1:
    numero1 = random.randint(1, 200)
    acertou1 = False
if quantidade_numeros >= 2:
    numero2 = random.randint(1, 200)
    # Garante que o segundo número seja diferente do primeiro
    while numero2 == numero1:
        numero2 = random.randint(1, 200)
    acertou2 = False

print("Qual o nível de dificuldade você gostaria de jogar?")
print("1 - Fácil (10 tentativas)")
print("2 - Médio (7 tentativas)")
print("3 - Difícil (5 tentativas)")

nivel = input("Escolha o nível de dificuldade (1, 2 ou 3): ")

if nivel == '1':
    tentativas = 10
elif nivel == '2':
    tentativas = 7
elif nivel == '3':
    tentativas = 5
else:
    print("Nível inválido")
    exit()

for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Adivinhe o número (entre 1 e 200): "))

    if quantidade_numeros >= 1 and not acertou1:
        if palpite == numero1:
            print("Parabéns! Você acertou o número 1!")
            acertou1 = True
        elif palpite < numero1:
            print(f"O número 1 é maior que {palpite}.")
        else:
            print(f"O número 1 é menor que {palpite}.")

    if quantidade_numeros >= 2 and not acertou2:
        if palpite == numero2:
            print("Parabéns! Você acertou o número 2!")
            acertou2 = True
        elif palpite < numero2:
            print(f"O número 2 é maior que {palpite}.")
        else:
            print(f"O número 2 é menor que {palpite}.")

    # Verifica se todos os números foram adivinhados
    if ((quantidade_numeros >= 1 and acertou1) and
        (quantidade_numeros < 2 or acertou2)):
        print("Você adivinhou todos os números! Parabéns!")
        break
else:
    print(f"Você não conseguiu adivinhar todos os números em {tentativas} tentativas.")
    if quantidade_numeros >= 1 and not acertou1:
        print(f"O número 1 era {numero1}.")
    if quantidade_numeros >= 2 and not acertou2:
        print(f"O número 2 era {numero2}.")
