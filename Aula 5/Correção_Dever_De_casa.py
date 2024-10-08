numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print(f"O número {numero} é divisível por 3.")
    if numero % 5 == 0:
        print(f"O número {numero} é divisível por 5.")
elif numero % 5 == 0:
        print(f"O número {numero} é divisível por 5.")
else:
    print(f"O número {numero} não é divisível nem por 3 nem por 5.")
