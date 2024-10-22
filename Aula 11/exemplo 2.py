# Função: Calcula o quadrado de um número



def quadrado(numero):
    return numero ** 2

numero = float(input("Digite um número: "))
resultado = quadrado(numero)  # Recebe o retorno da função
print(f"O quadrado de {numero} é {resultado}")
