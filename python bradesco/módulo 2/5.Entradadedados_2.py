import os


def limpar_terminal():
    os.system("clear || cls")


limpar_terminal()
codigo = int(input("Digite o código do produto: "))
limpar_terminal()
nome = input("Digite o nome do produto: ")
limpar_terminal()
salario = float(input("Digite o salário do funcionário: "))
ativo = True

limpar_terminal()
print("Código: %d" % codigo)
print("Nome: %s" % nome)
print("Salário: %.2f" % salario)
print("Ativo:", ativo)