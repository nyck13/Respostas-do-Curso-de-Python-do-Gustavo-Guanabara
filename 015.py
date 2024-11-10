dias = int(input('Informe a quantidade de dias que o carro foi utilizado: '))
km = float(input('Informe a quantidade de km percorridos: '))
valor = dias*60 + km*0.15
print('O valor total a ser pago é de R${:.2f}'.format(valor))