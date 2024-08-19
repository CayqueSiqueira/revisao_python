import os


fluxo_caixa = []

os.system("cls")

print("--------------------")
print("@ Fluxo de caixa @")
print("--------------------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para encerrar o programa #\n")

while True:

    opcao = int(input("Digite a opção desejada: "))


    # if opcao == 1:
    #     descricao = input("Digite a descrição da receita: ")
    #     valor = float(input("Digite o valor da receita: "))
    #     fluxo_caixa.append({
    #         "descricao": descricao, 
    #         "valor": valor
    #         })
    # elif opcao == 2:
    #     descricao = input("Digite a descrição da despesa: ")
    #     valor = float(input("Digite o valor da despesa: "))
    #     fluxo_caixa.append({
    #         "descricao": descricao, 
    #         "valor": valor
    #         })
    # else:
    #     break
    def adicionar_transacao(tipo):
        descricao = input(f"Digite a descrição da {tipo}: ")
        valor = float(input(f"Digite o valor da {tipo}: "))
        fluxo_caixa.append({
            "descricao": descricao, 
            "valor": valor
            })

    if opcao == 1:
        adicionar_transacao("receita")
    elif opcao == 2:
        adicionar_transacao("despesa")
    else:
        break

# nota fiscal
print("\n# Nota fiscal #")
total = 0
for fc in fluxo_caixa:
    print(f"descricao: {fc['descricao']} - valor: R$ {fc['valor']}")
    total += fc['valor']

