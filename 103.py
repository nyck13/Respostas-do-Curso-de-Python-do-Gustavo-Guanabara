def ficha(nome = '', gols = 0):
    if nome == '' and gols != 0:
        print(f'O jogador não informado marcou {gols} gols')
    elif nome != '' and gols == 0:
        print(f'{nome} não marcou gols ou não foi informado')
    elif nome == '' and gols == 0:
        print(f'O jogador não informado marcou nenhum gol ou não foi informado')
    else:
        print(f'{nome} marcou {gols} gols')

nome = str(input('Informe o seu nome: '))
gols = str(input('Informe a quantidade de gols do jogador: '))

if gols.isnumeric():
    gols = int(gols)
    ficha(nome, gols)
else:
    gols = 0
    ficha(nome, gols)