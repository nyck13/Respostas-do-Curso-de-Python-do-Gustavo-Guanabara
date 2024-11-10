lista = list()

while True:
    n = int(input('Digite um valor: '))

    if n in lista:
        print('Valor duplicado, não vou adicionar!')
    else:
        lista.append(n)

    resposta = str(input('Deseja continuar? [S]/[N] ')).strip().upper()
    if resposta == 'N':
        break

lista.sort()
print(f'A lista formada é: {lista}')