import os

os.system("cls")

print("---------------------")
print("|   Juros simples   |")
print("---------------------")

# formula do juros: J = PV * i * n 
# J = juros
# PV = valor presente
# i = taxa de juros - ao mês - convertida p decimal
# n = tempo - em meses

def calcular_valor_juros(pv, i, n):
    return pv * i * n

def calcular_taxa_juros(j, pv, n):
    return j / (pv * n)

def calcular_tempo_juros(j, pv, i):
    return j / (pv * i)

def calcular_valor_inicial(j, i, n):
    return j / (i * n)

# formula do valor futuro + juros FV = PV * (1 + i × n)
def calcular_valor_futuro(pv, i, n):
    return pv * (1 + i * n)

while True:
    print("Aplicação da formula de juros simples, entre com 'x' no que deseja calcular \nOs inputs seguem a ordem J = PV * i * n\n")
    j = input("Digite o valor dos juros: ")
    pv = input("Digite o valor inicial: ")
    i = input("Digite a taxa de juros (em %): ")
    n = input("Digite o tempo (em meses): ")

    if j.upper() == "X":
        tipojuros = input("Digite 1 para saber o valor do juros\nDigite 2 para o valor total acumulado\n")
        if tipojuros == '1':
            pv = float(pv)
            i = float(i) / 100
            n = float(n)
            print(f"O valor dos juros é R$ {calcular_valor_juros(pv, i, n):.2f}")
        elif tipojuros == '2':
            pv = float(pv)
            i = float(i) / 100
            n = float(n)
            print(f"O valor futuro é R$ {calcular_valor_futuro(pv, i, n):.2f}")
    elif pv.upper() == 'X':
        j = float(j)
        i = float(i) / 100
        n = float(n)
        print(f"O valor inicial é R$ {calcular_valor_inicial(j, i, n):.2f}")
    elif i.upper() == 'X':
        j = float(j)
        pv = float(pv)
        n = float(n)
        print(f"A taxa de juros é {calcular_taxa_juros(j, pv, n) * 100:.2f}%")
    elif n.upper() == 'X':
        j = float(j)
        pv = float(pv)
        i = float(i) / 100
        print(f"O tempo é {calcular_tempo_juros(j, pv, i)} meses")
    else:
        break
    if input("Deseja continuar? (s/n) ").upper() == 'N':
        break