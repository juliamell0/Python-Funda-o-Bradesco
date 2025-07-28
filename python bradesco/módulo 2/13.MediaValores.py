import os
os.system("clear || cls")

qtd = 0 
soma = 0
media = 0
valor = float(input('Digite um valor: '))

while (valor > 0):
    soma = soma + valor
    qtd = qtd + 1
    #entrada de valores
    valor = float(input('Digite um valor: '))

#Caso digite um valor negativo o laço encerra
media = soma / qtd
print(f'A soma dos valores digitados é: {soma}')
print(f'A quantidade de valores digitados é: {qtd}')
print(f'A média dos valores digitados é: {media}')