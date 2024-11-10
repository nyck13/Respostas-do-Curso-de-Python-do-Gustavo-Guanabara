from random import randint
from time import sleep
from operator import itemgetter

pessoas = {
    'pessoa1': randint(1,6),
    'pessoa2': randint(1, 6),
    'pessoa3': randint(1, 6),
    'pessoa4': randint(1, 6)
}

print('Valores sorteados:')
for k, v in pessoas.items():
    print(f'A {k} tirou {v} no dado.')
    sleep(1)

print('-------------------')
print('----- RANKING -----')
print('-------------------')
ranking = sorted(pessoas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]}')