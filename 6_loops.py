controle_entrada = int(input('Digite quantas notas deseja lançar: '))

notas = []
for i in range(controle_entrada):
    cod_aluno = int(input('Digite o código do aluno: '))
    nota = float(input('Digite a nota: '))
    resultado = [cod_aluno, nota]
    notas.append(resultado)


print("Quantidade de notas",len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print(f'O aluno de código {codigo_aluno} tirou a nota {nota}.')

#o mesmo pode ser feito usando while

# controle_entrada = int(input('Digite quantas notas deseja lançar: '))
# notas = []
# i = 0
# while i < controle_entrada:
#     cod_aluno = int(input('Digite o código do aluno: '))
#     nota = float(input('Digite a nota: '))
#     resultado = [cod_aluno, nota]
#     notas.append(resultado)
#     i += 1
# print("Quantidade de notas",len(notas))
# while i < len(notas):
#     codigo_aluno = notas[i][0]
#     nota = notas[i][1]
#     print(f'O aluno de código {codigo_aluno} tirou a nota {nota}.')
