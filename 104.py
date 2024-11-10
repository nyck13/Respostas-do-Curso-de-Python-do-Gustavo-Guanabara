def leiaint(string):
    numero = str(input(f'{string}'))
    while not numero.isnumeric():
        numero = str(input(f'{string}'))
    return float(numero)


n = leiaint('Informe um número: ')
print(f'Você acabou de digitar {n}')