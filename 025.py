nome = str(input('Informe qual é o seu nome: '))
nome = nome.upper()
nome = nome.strip()
print('O seu nome possui "Silva"? {}'.format(nome.find('SILVA') >= 0))