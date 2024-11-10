numeros = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))
print('O número 9 apareceu {} vezes'.format(numeros.count(9)))
if 3 in numeros:
    print('O número 3 foi digitado pela primeira vez na posição {}'.format(numeros.index(3)))
else:
    print('O valor 3 não foi digitado!')
print('Números pares: ', end= '')
for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=' ')