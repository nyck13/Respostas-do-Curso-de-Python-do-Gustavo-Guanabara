import random
from time import sleep
print('===============================================')
print('====== BEM-VINDO AO JOGO DA ADIVINHAÇÃO =======')
print('===============================================')

numero = random.randint(0, 5)

tentativa = int(input('A máquina já pensou no número, qual será sua primeira tentativa? '))
print('PROCESSANDO')
sleep(2)
if(tentativa == numero):
    print('Parabéns, você acertou e o número correto é {}!'.format(numero))
else:
    print('Eitaa, você errou! O número correto é {}'.format(numero))

