print('===================================================')
print('====== Bem-vindo ao analisador de triângulos ======')
print('===================================================')

l1 = float(input('Informe o valor do primeiro lado: '))
l2 = float(input('Informe o valor do segundo lado: '))
l3 = float(input('Informe o valor do terceiro lado: '))

if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    print('É possível se montar um triângulo de lados {}, {} e {}'.format(l1, l2, l3))
else:
    print('Não é possível se montar um triângulo de lados {}, {} e {}'.format(l1, l2, l3))