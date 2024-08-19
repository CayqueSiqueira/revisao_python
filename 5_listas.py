# append acrescenta um item ao final da lista
# inset insere um item em uma posição específica
# pop sem parametro remove o último item da lista
# pop com parametro remove o item de acordo com a posição
# sort ordena a lista
# reverse inverte a lista
# index retorna a posição de um item
# count conta quantas vezes um item aparece na lista
# remove remove a primeira ocorrência de um item

lista = [1, 2, 3, 4, 5]
print(lista)
lista.append(6)
print(lista)
lista.insert(0, 0)
print(lista)
lista.pop()
print(lista)
lista.pop(0)
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
print(lista.index(1))
print(lista.index(2))
print(lista.index(3))
print(lista.index(4))
lista.insert(0, 3)
print(lista.count(3))
lista.remove(3)
print(lista)

