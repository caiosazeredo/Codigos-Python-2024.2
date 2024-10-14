# Programa de reciclagem com contagem de materiais

print("Bem-vindo ao programa de reciclagem!")

# Inicializa o contador de cada material
contador_papel = 0
contador_plastico = 0
contador_vidro = 0
contador_metal = 0
contador_outros = 0

continuar = 's'

while continuar.lower() == 's':
    # Solicita ao usuário o tipo de material para reciclar
    material = input("Digite a lixeira para reciclar (papel, plástico, vidro, metal): ").lower()
    lixo = input("Digite o nome do lixo: ").lower()
    # Verifica e contabiliza o material
    if material == 'papel':
        if lixo == "caixa" or lixo == "carta" or lixo == "cartolina":
            print("Lixeira correta!")
            contador_papel += 1
    

# Exibe o resumo da reciclagem
print("\nResumo da reciclagem:")
print(f"Papel reciclado: {contador_papel}")
print(f"Plástico reciclado: {contador_plastico}")
print(f"Vidro reciclado: {contador_vidro}")
print(f"Metal reciclado: {contador_metal}")
print(f"Materiais não reconhecidos ou não recicláveis: {contador_outros}")

print("\nObrigado por contribuir com a reciclagem!")
