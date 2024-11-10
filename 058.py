import random
from time import sleep
print('===============================================')
print('====== BEM-VINDO AO JOGO DA ADIVINHAÇÃO =======')
print('===============================================')

numero = random.randint(0, 10)
qntdPalpites = 0

tentativa = int(input('A máquina já pensou no número, qual será sua primeira tentativa? '))
print('PROCESSANDO')
sleep(1)

while tentativa != numero:
    qntdPalpites += 1
    tentativa = int(input('Você errou! Informe outro número: '))
    print('PROCESSANDO')
    sleep(1)
print('Parabéns, você acertou com {} tentativas e o número correto é {}!'.format(qntdPalpites, numero))


