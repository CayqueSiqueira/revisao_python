# def minha_funcao(val1, val2):
#     return val1 + val2

# resposta = minha_funcao(1, 2)

# print(resposta) 


def minha_funcao(val1, val2):
    return val1 + val2

while True:
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite outro valor: "))

    reposta = minha_funcao(valor1, valor2)
    print(reposta)

    if input("Deseja continuar? (s/n) ") == 'n':
        break