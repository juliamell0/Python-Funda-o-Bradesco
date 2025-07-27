import os
os.system("clear || cls")
nota1=float(input("Informe a primeira nota: "))
nota2=float(input("Informe a segunda nota: "))

#calcular media
mediafinal = (nota1 + nota2) / 2

#verificação
if mediafinal >= 7:
    print(f'Média: {mediafinal} - Aprovado!')
else:
    print(f'Média: {mediafinal} - Reprovado!')