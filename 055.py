maiorPeso = 0
menorPeso = 0

for i in range(0, 5):
    peso = float(input('Informe o valor do peso: '))
    if i == 0:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso

print('O menor peso foi de {:.2f}Kg e o maior peso foi de {:.2f}Kg'.format(menorPeso, maiorPeso))