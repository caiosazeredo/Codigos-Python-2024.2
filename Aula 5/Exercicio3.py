print("Bem-vindo ao Lava rapido Rapid")
tipolavagem = int(input("Selecione o tipo da lavagem \n 1- Lavagem Completa a R$50.00 \n 2- Lavagem básica a R$35.00"))
if(tipolavagem == 1):
    print("Você selecionou a lavagem completa")
    valortotal = 50
    categorialavagem = "completa"
elif(tipolavagem == 2):
    print("Você selecionou a lavagem basica")
    valortotal = 35
    categorialavagem = "basica"
else:
    print("numero invalido, tente novamente")
pretinho = input("Gostaria de adicionar o pretinho na roda por mais R$5,00? (Sim ou Não)").lower()
if(pretinho == "sim"):
    valortotal += 5
    print(f"o Serviço de {categorialavagem} será no total de R${valortotal} com pretinho")
else:
    print(f"o Serviço de {categorialavagem} será no total de R${valortotal}")