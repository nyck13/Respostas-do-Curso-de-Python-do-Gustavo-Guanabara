from random import randint

print('========================')
print('VAMOS JOGAR ÍMPAR OU PAR')
print('========================')

vitorias = 0

while True:
    nMaquina = randint(0,10)
    nJogador = int(input('Informe um valor: '))
    imparOUpar = str(input('Ímpar ou par [I]/[P]: ')).strip().upper()
    soma = nMaquina + nJogador
    if soma%2 == 0:
        if imparOUpar == 'P':
            print('A máquina escolheu {} e você escolheu {}, a soma dos dois é {} que é par'.format(nMaquina, nJogador, soma))
            vitorias += 1
        else:
            print('Você perdeu, a máquina escolheu {} e você escolheu {}, a soma dos dois é {} que é par'.format(nMaquina, nJogador, soma))
            break
    else:
        if imparOUpar == 'I':
            print('A máquina escolheu {} e você escolheu {}, a soma dos dois é {} que é ímpar'.format(nMaquina, nJogador, soma))
            vitorias += 1
        else:
            print('Você perdeu, a máquina escolheu {} e você escolheu {}, a soma dos dois é {} que é ímpar'.format(nMaquina, nJogador, soma))
            break
print('Você conseguiu uma sequência de {} acertos'.format(vitorias))