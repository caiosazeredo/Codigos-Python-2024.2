
poderes = ["choque do trovão", "calda de ferro", "ataque rapido", "esquiva"]

print("Poderes do pikachu:", poderes)
validacao = input("Gostaria de adicionar um poder novo ao Pikachu?S/N:").lower()
if validacao == "s":
    adicionar = input("Qual poder gostaria de adicionar?").lower()
    remover = input("Qual poder gostaria de remover?").lower()
    poderes.remove(remover)
    poderes.append(adicionar)

print("Poderes após atualização:", poderes)
