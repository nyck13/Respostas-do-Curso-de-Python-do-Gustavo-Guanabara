from random import randint

itens = ('pedra', 'papel', 'tesoura')
jSistema = randint(0,2)
jUsuario = int(input('''Suas opções:
[0] PEDRA 
[1] PAPEL
[2] TESOURA
Qual a sua jogada? '''))

if jUsuario != 0 and jUsuario != 1 and jUsuario != 2:
    print('Jogada inválida!')
    exit()

print('Você jogou {}'.format(itens[jUsuario]))
print('A máquina jogou {}'.format(itens[jSistema]))

if jSistema == jUsuario:
    print('Deu empate, pois vocês escolheram a mesma coisa!')
elif jSistema == 0 and jUsuario == 1:
    print('Você ganhou, pois o papel envolve a pedra!')
elif jSistema == 0 and jUsuario == 2:
    print('Você perdeu, pois a pedra quebra a tesoura!')
elif jSistema == 1 and jUsuario == 0:
    print('Você perdeu, pois o papel envolve a pedra!')
elif jSistema == 1 and jUsuario == 2:
    print('Você ganhou, pois a tesoura corta o papel!')
elif jSistema == 2 and jUsuario == 0:
    print('Você ganhou, pois a pedra quebra a tesoura!')
elif jSistema == 2 and jUsuario == 1:
    print('Você ganhou, pois a tesoura corta o papel!')