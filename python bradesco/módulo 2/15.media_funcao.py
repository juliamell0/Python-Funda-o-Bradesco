import os
os.system("clear || cls ")


def lernotas():
    nota = float(input(f"Digite a nota: "))
    return nota
    
def resultado(nota1,nota2):
    media = (nota1 + nota2) / 2
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    if media >= 7:
        print(f"Aprovado com média {media:.1f}")
    else:
        print(f"Reprovado com média {media:.1f}")

a= lernotas()
b = lernotas()
resultado(a, b) 

