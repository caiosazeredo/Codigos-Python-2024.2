#Selecione 1 para barbaro, 2 para mago e 3 para arqueiro
SelecaoClasse = int(input("Selecione a classe que gostaria de jogar! \n Digite 1 para Guerreiro \n Digite 2 para mago \n Digite 3 para arqueiro \n"))
if(SelecaoClasse == 1):
    classe="Guerreiro"
elif(SelecaoClasse == 2):
    classe="Mago"
elif(SelecaoClasse == 3):
    classe="Arqueiro"
else:
    classe="invalida"
print(f"A classe que você selecionou é {classe} \n")

SelecaoEquipamento = int(input("Selecione o equipamento para seu personagem: \n Digite 1 para arma de curto alcance \n Digite 2 para arma de longo alcance \n\n"))
if (SelecaoEquipamento == 1):
    equipamento = "de curto alcance"
elif (SelecaoEquipamento == 2):
    equipamento = "de longo alcance"
else:
    equipamento = "invalida"
print(f"A classe que você selecionou é {classe}\n")

if equipamento != "invalida" and classe != "invalida":
        print(f"Personagem criado com sucesso! \n Vocé um {classe} com o equipamento {equipamento}")
else:
    print("Erro na criação do personagem, tente novamente!")
