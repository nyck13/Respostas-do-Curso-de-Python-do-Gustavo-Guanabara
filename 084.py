pessoas = list()
maiorPeso = menorPeso = 0
while True:
    info = [str(input('Infome o seu nome: ')),
            int(input('Informe o seu peso: '))]

    if len(pessoas) == 0:
        maiorPeso = menorPeso = info[1]
    else:
        if info[1] > maiorPeso:
            maiorPeso = info[1]
        if info[1] < menorPeso:
            menorPeso = info[1]
    pessoas.append(info[:])

    resposta = str(input('Deseja continuar? [S]/[N]'))
    if resposta in 'Nn':
        break

print(f'A quantidade de pessoas na lista é {len(pessoas)}')
print(f'O maior peso é {maiorPeso} de ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso é {menorPeso} de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'{p[0]}', end=' ')