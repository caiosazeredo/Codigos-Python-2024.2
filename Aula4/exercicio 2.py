rodas = int(input("quantas rodas tem o veículo?"))
if(rodas == 4):
    print("O veículo é um carro ou van")
elif (rodas == 2):
    print("O veículo é uma moto ou bicicleta")
elif(rodas== 1):
    print("O veículo é um monociclo")
elif(rodas==6):
    print("o veículo é um ônibus")
elif(rodas>=8 and rodas<=20):
    print("o veículo é provavelmente um caminhão")
else:
    print("não foi encontrado um veículo correspondente ao numero de rodas")
