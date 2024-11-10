n = int(input('Informe um número inteiro? '))
print('''Qual será a base de conversão?'
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input('Informe a sua opção: '))
if opcao == 1:
    print('O número {} em binário é {}'.format(n, bin(n)))
elif opcao == 2:
    print('O número {} em octal é {}'.format(n, oct(n)))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(n, hex(n)))
else:
    print('Não foi possível realizar a conversão de {}, informe um valor válido!'.format(n))