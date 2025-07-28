import os
os.system("clear || cls")

idade = int(input("Informe sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 16:
    print("Infanto juvenil")
else:
    print("Menor de idade")