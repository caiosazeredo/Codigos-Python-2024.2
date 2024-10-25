import time
import random
aventureiro = [
    ["Vida", "Ataque base"],
    [1000, 20]
]
assaltante = [
    ["Vida", "Ataque base"],
    [600, 20]
]

while assaltante[1][0] > 0 and aventureiro[1][0] > 0:
    Variavelaventureiro = random.randint(1, 20)
    Variaveassaltante = random.randint(1, 20)
    assaltante[1][0] -= 20 * Variaveassaltante
    aventureiro[1][0] -= 20 * Variaveassaltante
    print("Status aventureiro:")
    for linha in aventureiro:
        print(linha)
    print(f"multiplicador de critico:", Variavelaventureiro)
    print("Status assaltante:")
    for linha in assaltante:
        print(linha)
    print(f"multiplicador de critico:", Variaveassaltante)
    time.sleep(4)
