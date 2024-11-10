comprimento = float(input('Informe o comprimento da parede: '))
largura = float(input('Informe a largura da parede: '))
area = comprimento*largura
quantidadeTinta = area/2
print('A quantidade de tinta necessária para pintar essa parede é {} litros'.format(quantidadeTinta))