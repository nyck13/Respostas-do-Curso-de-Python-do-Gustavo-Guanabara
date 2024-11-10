soma = 0
for i in range(0, 6):
    n = int(input('Informe o valor {}: '.format(i+1)))
    if n%2 == 0:
        soma = soma + n
print('A soma dos números é {}'.format(soma))