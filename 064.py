n = int(input('Qual o seu número: '))
contador = somaTotal = 0

while n != 999:
    somaTotal += n
    contador += 1
    n = int(input('Qual o seu número: '))

print('Foram digitado {} números e a soma entre todos vale {}'.format(contador, somaTotal))
