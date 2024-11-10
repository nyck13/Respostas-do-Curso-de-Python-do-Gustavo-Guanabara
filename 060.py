n = int(input('Informe o número que você deseja saber o fatorial: '))
total = 1
contador = 1

while contador <= n:
    total = total*contador
    contador += 1

print('O valor de {}! é {}'.format(n, total))