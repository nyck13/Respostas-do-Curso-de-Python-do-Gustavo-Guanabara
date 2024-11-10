n = str(input('Informe qual o seu nome: ')).strip()
nome = n.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[-1]))