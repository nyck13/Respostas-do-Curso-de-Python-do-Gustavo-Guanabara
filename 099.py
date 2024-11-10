from time import sleep
from random import randint

def maior(*lista):
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Analisando os valores passados...')
    contador = maiorValor = 0
    for valor in lista:
        print(f'{valor}', end=' ')
        if valor > maiorValor:
            maiorValor = valor
        contador += 1
    print(f'Foram informados {contador} valores')
    print(f'O maior valor é de {maiorValor}')
    sleep(1)

maior(randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9))
maior(randint(1, 9))
maior()
