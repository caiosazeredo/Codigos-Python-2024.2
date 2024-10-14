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
    material = input("Digite o tipo de material para reciclar (papel, plástico, vidro, metal): ").lower()
    
    # Verifica e contabiliza o material
    if material == 'papel':
        print("Papel deve ser colocado na lixeira azul.")
        contador_papel += 1
    elif material == 'plástico' or material == 'plastico':
        print("Plástico deve ser colocado na lixeira vermelha.")
        contador_plastico += 1
    elif material == 'vidro':
        print("Vidro deve ser colocado na lixeira verde.")
        contador_vidro += 1
    elif material == 'metal':
        print("Metal deve ser colocado na lixeira amarela.")
        contador_metal += 1
    else:
        print("Material não reconhecido ou não reciclável.")
        contador_outros += 1
    
    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja reciclar outro material? (s/n): ")

# Exibe o resumo da reciclagem
print("\nResumo da reciclagem:")
print(f"Papel reciclado: {contador_papel}")
print(f"Plástico reciclado: {contador_plastico}")
print(f"Vidro reciclado: {contador_vidro}")
print(f"Metal reciclado: {contador_metal}")
print(f"Materiais não reconhecidos ou não recicláveis: {contador_outros}")

print("\nObrigado por contribuir com a reciclagem!")
