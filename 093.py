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

print('================================================')
print(jogador)
print('================================================')
print(f'O campo nome tem o valor {jogador['nome']}')
print(f'O campo gols tem o valor {jogador['gols']}')
print(f'O campo total tem o valor {jogador['total']}')
print('================================================')
print(f'O jogador {jogador['nome']} jogou {jogos} partidas')
for i in range(0, jogos):
    print(f'=> Na partida {i+1}, fez {gols[i]}')
print(f'Foi um total de {nGols}')