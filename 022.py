nome = str(input('Informe qual o seu nome completo: '))
print('O seu nome em letras maiusculas é {}'.format(nome.upper()))
print('O seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome ao todo possui {} letras'.format(len(nome) - nome.count(' ')))

nome = nome.split()
print('O seu primeiro nome é {} e possui {} letras'.format(nome[0], len(nome[0])))