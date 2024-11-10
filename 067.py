while True:
    numero = int(input('Informe qual número você quer a tabuada: '))
    if numero >= 0:
        print('-------------------')
        contador = 0
        while contador < 10:
            print('{}x{} = {}'.format(contador+1, numero, (contador+1)*numero))
            contador += 1
        print('-------------------')
    else:
        print('Programa encerrado!')
        break