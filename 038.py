n1 = float(input('Infome o primeiro valor: '))
n2 = float(input('Infome o segundo valor: '))

if n1 > n2:
    print('O primeiro valor é maior, ou seja, {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor é maior, ou seja, {} é maior que {}'.format(n2, n1))
else:
    print('Os dois valores inseridos são iguais!')