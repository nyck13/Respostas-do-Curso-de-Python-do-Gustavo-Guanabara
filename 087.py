matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceiraColuna = maiorSegundaLinha = 0

for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Informe o valor para [{l},{c}]: '))
        matriz[l][c] = n
        if n%2 == 0:
            somaPares += n
        if c == 2:
            somaTerceiraColuna += n
        if l == 1 and c == 0:
            maiorSegundaLinha = n
        elif l == 1 and c != 0:
            if n > maiorSegundaLinha:
                maiorSegundaLinha = n

print('=========================')

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()

print(f'A soma de todos os valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior termo da segunda linha é {maiorSegundaLinha}')