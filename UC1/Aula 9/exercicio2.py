import random

numero = random.randint(1, 200)
tentativas = 10

for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Adivinhe o número (entre 1 e 200): "))
    if palpite == numero:
        print("Parabéns! Você acertou o número.")
    elif palpite < numero:
        print("O número é maior.")
    else:
        print("O número é menor.")
else:
    print(f"Você não conseguiu adivinhar o número em {tentativas} tentativas. O número era {numero}.")
