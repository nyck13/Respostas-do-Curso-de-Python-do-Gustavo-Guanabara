velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade <= 80:
    print('Tudo certo, dirija com segurança!')
else:
    print('Reduza a velocidade, você cometeu uma infração e pagará R${},00'.format((velocidade - 80)*7))