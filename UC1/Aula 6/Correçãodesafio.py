EscolhaLanche = int(input("-------------------Bem Vindo ao Maquimeleca, qual opção você gostaria?---------------------\n Digite 1 para Hamburguer - R$10,00 \n Digite 2 para Batata Frita  - R$10,00 \n Digite 3 para refrigerente - R$10,00 \n Digite 4 para combo (os 4 itens) - R$22,00 \n"))
if EscolhaLanche == 4:
    print("Muito bem, o combo será sairá a R$22,00")
    exit()
if EscolhaLanche == 1:
    escolha = "Hamburguer"
    itemadicional1 = "Batata Frita"
    itemadicional2 = "Refrigerante"
if EscolhaLanche == 2:
    escolha = "Batata Frita"
    itemadicional1 = "Hamburguer"
    itemadicional2 = "Refrigerante"
if EscolhaLanche == 3:
    escolha = "Refrigerante"
    itemadicional1 = "Batata Frita"
    itemadicional2 = "Hamburguer"

Complemento = input(f"Você adicionou {escolha}  Gostaria de {itemadicional1} ou {itemadicional2} (s/n)? \n").lower()

if(Complemento == "s"):
    decisaocomplemento = int(input(f"muito bem! Digite 1 para {itemadicional1} ou 2 para {itemadicional2}?"))
    if(decisaocomplemento == 1):
        convencercliente = input(f"Gostaria de adicionar o {itemadicional2} por mais R$2,00? (s/n)").lower()
        if (convencercliente == "s" ):
            print("Otimo, o seu pedido custou R$22,00")
        else:
            print("Sem problemas, o seu pedido custou R$20,00")
    else:
        convencercliente = input(f"Gostaria de adicionar o {itemadicional1} por mais R$2,00? (s/n)").lower()
        if (convencercliente == "s" ):
            print("Otimo, o seu pedido custou R$22,00")
        else:
            print("Sem problemas, o seu pedido custou R$20,00")
else:
    print(f"Muito bem, seu pedido de {escolha} custará R$10,00")
