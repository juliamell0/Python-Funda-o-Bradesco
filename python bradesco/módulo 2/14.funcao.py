import os
os.system("clear || cls ")



#Return: Deve ser utilizado quando houver necessidade de retornar alguma informação para a ação da função.

def mensagem1():
    print("Olá, seja bem-vindo(a) ao curso de Python!")

def mensagem2():
    return "Olá, seja bem-vindo(a) ao curso de Python!"

mensagem1()  # Chamada da função que imprime a mensagem diretamente
texto = mensagem2()  # Chamada da função que retorna a mensagem
print(texto)  # Exibe a mensagem retornada pela função