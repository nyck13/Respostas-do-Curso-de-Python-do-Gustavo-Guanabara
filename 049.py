numero = int(input('Informe qual número você deseja ver a tabauda: '))
print('Tabuada do {}'.format(numero))
for i in range(1, 11):
    print('{}x{} = {}'.format(i, numero, i*numero))