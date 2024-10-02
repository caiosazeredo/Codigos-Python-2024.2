print ("Qual sua idade?")
idade = int(input())
valor_calca_azul = 120
valor_jaqueta_verde = 150
valor_com_desconto_calca_azul = valor_calca_azul - idade
valor_com_desconto_jaqueta_verde = valor_jaqueta_verde - idade
print (f"Na nossa loja temos os seguintes produtos: Calça azul com o valor {valor_calca_azul} e uma jaqueta verde com o valor {valor_jaqueta_verde}")
print(f"Graças a sua idade, nos daremos um desconto de R${idade} para você nos dois produtos!")
print(f"A calça azul custará {valor_com_desconto_calca_azul} e a jaqueta custará {valor_com_desconto_jaqueta_verde}")
