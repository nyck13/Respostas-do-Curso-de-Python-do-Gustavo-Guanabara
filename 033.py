num1 = float(input('Informe o valor do primeiro número: '))
num2 = float(input('Informe o valor do segundo número: '))
num3 = float(input('Informe o valor do terceiro número: '))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print('O maior número é {} e o menor número é {}'.format(num1, num3))
    else:
        print('O maior número é {} e o menor número é {}'.format(num1, num2))
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print('O maior número é {} e o menor número é {}'.format(num2, num3))
    else:
        print('O maior número é {} e o menor número é {}'.format(num2, num1))
else:
    if num1 > num2:
        print('O maior número é {} e o menor número é {}'.format(num3, num2))
    else:
        print('O maior número é {} e o menor número é {}'.format(num3, num1))
