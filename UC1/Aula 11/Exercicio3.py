# Função: Converte de Celsius para Fahrenheit
def converter(celsius):
    return (celsius * 9/5) + 32
    

celsius = float(input("Digite a temperatura em Celsius: "))
resultado = converter(celsius)  # Recebe o retorno da função
print(f"A temperatura de {celsius}°C é equivalente a {resultado}°F")
