import os
os.system("clear || cls")


#Formatação de variáveis, A formatação de variáveis em Python,
#especialmente dentro de strings, serve para apresentar dados de maneira 
# mais legível e organizada, seja controlando o número de casas decimais de um número,
#  adicionando formatação monetária, ou incluindo variáveis em mensagens de texto de 
# forma clara e concisa. 
codigo = 105
nome = "João"
salario = 2500.50
ativo = True

print("Código: %d" % codigo)
print("Nome: %s" % nome)
print("Salário: %.2f" % salario)
print("Ativo:", ativo)

