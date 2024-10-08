EscolhaLanche = int(input("-------------------Bem Vindo ao Maquimeleca, qual opção você gostaria?---------------------\n Digite 1 para Hamburguer - R$10,00 \n Digite 2 para Batata Frita  - R$10,00 \n Digite 3 para refrigerente - R$10,00 \n Digite 4 para combo (os 4 itens) - R$22,00 \n"))
item1 = "Hamburguer"
item2 = "Batata Frita"
item3 = "Refrigerante"
item4 = "Combo"

if(EscolhaLanche == 1):
    print(f"Você escolheu {item1}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 2 para Batata Frita e Digite 3 para refrigerente \n"))
    if (adicional == 2):
        print(f"Você escolheu {item1} e {item2}")
        oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item1} + {item2},  totalizando R$20,00")
    elif (adicional == 3):
        print(f"Você escolheu {item1} e {item3} \n")
        oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item1} + {item3},  totalizando R$20,00")
    else:
        print(f"Seu pedido é {item1},  totalizando R$10,00")
#elif(EscolhaLanche == 2):
    #completar o codigo
#elif(EscolhaLanche == 3):
    #completar o codigo