from math import factorial

def fatorial(numero, show=False):
    if not show:
        print(factorial(numero))
    else:
        for i in range(1, numero + 1):
            print(f'{i}', end=' ')
            if i < numero:
                print(f'x', end=' ')
        print(f'= {factorial(numero)}')

fatorial(5, show=False)