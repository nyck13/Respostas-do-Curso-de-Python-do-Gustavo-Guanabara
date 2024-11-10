import moeda

p = float(input('Informe o preço: '))
print(f'A metade de {moeda.formatar(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.dobrar(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')