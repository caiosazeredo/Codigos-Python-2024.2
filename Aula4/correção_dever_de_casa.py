
# Solicita o tamanho do aro da roda

aro = float(input("Digite o tamanho do aro da roda da bicicleta (em polegadas): "))
# Calcula o tamanho dos componentes com base no aro
tamanho_guidao = aro / 2
tamanho_manete = aro / 4
tamanho_quadro = aro

# Exibe as recomendações
print(f"Tamanho recomendado do guidão: {tamanho_guidao:.2f} polegadas")
print(f"Tamanho recomendado da manete: {tamanho_manete:.2f} polegadas")
print(f"Tamanho recomendado do quadro: {tamanho_quadro:.2f} polegadas")

