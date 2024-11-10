n = int(input('Informe um valor: '))
contador = 1
somaTotal = maiorValor = menorValor = n
continar = str(input('Quer continuar? [S]/[N] ')).strip().upper()

while continar == 'S':
    contador += 1
    n = int(input('Informe um valor: '))
    somaTotal += n
    if n > maiorValor:
        maiorValor = n
    if n < menorValor:
        menorValor = n
    continar = str(input('Quer continuar? [S]/[N] ')).strip().upper()

print('A média dos valores foi de {:.2f}, o menor valor foi {} e o maior valor foi {}'.format(somaTotal/contador, menorValor, maiorValor))

