lista = list()
listaPares = list()
listaImpares = list()

while True:
    n = int(input('Informe um valor: '))
    lista.append(n)
    resposta = str(input('Deseja continuar? [S]/[N]')).strip().upper()
    if resposta == 'N':
        break

lista.sort()

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listaPares.append(lista[i])
    else:
        listaImpares.append(lista[i])

print(f'Lista informada: {lista}')
print(f'Lista pares: {listaPares}')
print(f'Lista ímpares: {listaImpares}')