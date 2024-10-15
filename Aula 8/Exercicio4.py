#Programa que pede 4 numeros e faz a soma deles caso sejam impares
soma = 0
for i in range (4):
    numero = int(input("Digite um numero:"))
    if numero % 2 != 0:
        soma+= numero
print("A soma é:")
print(soma)
