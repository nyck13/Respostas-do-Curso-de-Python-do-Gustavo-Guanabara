from random import randint
from time import sleep

print('=====================')
print('  JOGOS DA MEGASENA  ')
print('=====================')

jogos = int(input('Qual a quantidade de jogos desejada? '))
lista = []
contador = 0

for i in range(0, jogos):
    while contador < 6:
        while True:
            n = randint(1, 60)
            if n not in lista:
                lista.append(n)
                contador += 1
            if contador >= 6:
                break
    lista.sort()
    print(lista)
    lista.clear()
    sleep(2)
    contador = 0