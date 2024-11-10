listaTotal = list()
listaPares = list()
listaImpares = list()

for i in range(0, 7):
    n = int(input(f'Informe o {i+1}o. valor: '))
    if n % 2 == 0:
        listaPares.append(n)
    else:
        listaImpares.append(n)

listaPares.sort()
listaImpares.sort()
listaTotal.append(listaPares)
listaTotal.append(listaImpares)

print(f'Os valores pares digitados: {listaPares}')
print(f'Os valores ímpares digitados: {listaImpares}')