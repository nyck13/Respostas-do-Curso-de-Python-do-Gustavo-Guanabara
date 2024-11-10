lista = list()

while True:
    jogador = {
        'nome':str(input('Qual o nome do jogador: '))
    }
    gols = list()

    nGols = 0
    jogos = int(input('Informe a quantidade de jogos: '))
    for i in range(0, jogos):
        n = int(input(f'Quantos gols na partida {i+1}: '))
        gols.append(n)
        nGols += n
    jogador['gols'] = gols
    jogador['total'] = nGols
    lista.append(jogador.copy())

    resposta = str(input('Deseja continuar? [S]/[N] ')).strip().upper()
    if resposta == 'N':
        break
    jogador.clear()

print(lista)
print('--------------------------------------------')
print('Cód  Nome             Gols             Total')
print('--------------------------------------------')
for k, v in enumerate(lista):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<17}', end='')
    print()
print('--------------------------------------------')

while True:
    n = int(input('Mostrar dados de qual jogador? (999 STOP) '))
    if n != 999:
        print(f'Levantamento do jogador {lista[n]["nome"]}')
        for i, g in enumerate(lista[n]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    else:
        break