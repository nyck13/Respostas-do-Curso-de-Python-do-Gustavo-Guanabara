lista = list()

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)

    resposta = str(input('Deseja continuar? [S]/[N] ')).strip().upper()
    if resposta == 'N':
        break

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')