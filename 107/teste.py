import moeda

p = float(input('Informe o preço: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobrar(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')