n = str(input('Informe o valor do seu número: '))
n = n.strip('')

print('Número de unidades: {}'.format(n[3]))
print('Número de dezenas: {}'.format(n[2]))
print('Número de centenas: {}'.format(n[1]))
print('Número de milhares: {}'.format(n[0]))