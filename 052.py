n = int(input('Informe o valor que você deseja saber se é número primo: '))
soma = 0
for i in range(2, n):
    if n%i == 0:
        soma = soma + 1
if soma == 0:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))