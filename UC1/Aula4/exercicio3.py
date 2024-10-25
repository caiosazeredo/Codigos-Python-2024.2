peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Classifica o IMC com base nas condições
if (imc < 18.5):
    classificacao = "MAGREZA"
    grau = 0
elif (18.5 <= imc < 25):
    classificacao = "NORMAL"
    grau = 0
elif (25 <= imc < 30):
    classificacao = "SOBREPESO"
    grau = 1
elif (30 <= imc < 40):
    classificacao = "OBESIDADE"
    grau = 2
else:
    classificacao = "OBESIDADE GRAVE"
    grau = 3

# Exibe os resultados
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Grau de obesidade: {grau}")