from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('A lista de números sorteada: {}'.format(numeros))
print('O valor máximo é {} e o valor mínimo é {}'.format(max(numeros), min(numeros)))