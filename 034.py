salario = float(input('Informe o valor do seu salario: '))
if salario > 1250:
    print('O valor do seu aumento será de {:.2f}'.format(salario * 0.1))
else:
    print('O valor do seu aumento será de {:.2f}'.format(salario * 0.15))