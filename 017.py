import math

catetoAdjacente = float(input('Informe o valor do cateto adjacente: '))
catetoOposto = float(input('Informe o valor do cateto oposto: '))

hipotenusa = math.sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))
print('O valor da hipótenusa é de {:.2f}'.format(hipotenusa))