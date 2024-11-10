from random import randint

def sorteia(quantidade):
    lista = list()
    print('Sorteando ', end='')
    for i in range(0, quantidade):
        n = randint(1, 9)
        print(f'{n}', end=' ')
        lista.append(n)
    print()
    return lista

def somaPar(lista):
    total = 0
    for valor in lista:
        if valor % 2 == 0:
            total += valor
    print(f'Somando os valores pares de {lista}, temos {total}')

somaPar(sorteia(5))