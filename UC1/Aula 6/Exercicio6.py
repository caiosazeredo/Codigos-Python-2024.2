# calculadora

Numero1 = float(input("Digite o primeiro número: \n "))
Numero2 = float(input("Digite o segundo número: \n "))

escolha = input("Digite o número da operação desejada: \n1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão\n")


if escolha == '1':
    resultado = Numero1 + Numero2
    print(f"\nResultado da soma: {Numero1} + {Numero2} = {resultado}")
elif escolha == '2':
    resultado = Numero1 - Numero2
    print(f"\nResultado da subtração: {Numero1} - {Numero2} = {resultado}")
elif escolha == '3':
    resultado = Numero1 * Numero2
    print(f"\nResultado da multiplicação: {Numero1} * {Numero2} = {resultado}")
elif escolha == '4':
    # Verifica se o segundo número é zero antes de dividir
    if Numero2 != 0:
        resultado = Numero1 / Numero2
        print(f"\nResultado da divisão: {Numero1} / {Numero2} = {resultado}")
    else:
        print("\nErro: Divisão por zero não é permitida!")
else:
    print("\nOpção inválida. Tente novamente.")
