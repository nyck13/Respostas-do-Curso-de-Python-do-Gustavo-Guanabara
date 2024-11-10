import moeda

p = float(input('Informe o preço: '))
print(f'A metade de {moeda.formatar(p)} é {moeda.formatar(moeda.metade(p))}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.formatar(moeda.dobrar(p))}')
print(f'Aumentando 10%, temos {moeda.formatar(moeda.aumentar(p, 10))}')