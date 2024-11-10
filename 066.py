contador = 0
soma = 0

while True:
    n = int(input('Informe o seu número [999 para encerrar]: '))
    if n != 999:
        contador += 1
        soma += n
    else:
        break
print('A quantidade de números informados é de {} e a soma de todos eles é {}'.format(contador, soma))