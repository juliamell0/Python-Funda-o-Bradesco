import os
os.system("clear || cls")

a = input("Informe um valor para a variável a: ")
b = input("Informe um valor para a variável b: ")

if (a>b):
    aux=a
    a=b
    b=aux
print("O valor da variável a agora é:", a)
print("O valor da variável b agora é:", b)

# "aux" geralmente refere-se a uma variável auxiliar. Essa variável é utilizada
# para armazenar temporariamente um valor durante a execução de um algoritmo, muitas 
# vezes para facilitar a troca de valores entre outras variáveis ou para realizar 
# cálculos intermediários. 
#Exemplo: Para trocar os valores de duas variáveis x e y sem perder nenhum dos valores 
# originais, é comum utilizar uma variável auxiliar aux