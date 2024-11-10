print('========================================')
print('======== SEQUÊNCIA DE FIBONACCI ========')
print('========================================')

n = int(input('Informe a quantidade de termos: '))
termoAnterior = 0
termoAtual = 1
contador = 1

if n == 1:
    print(termoAnterior, end=' ')
    exit()
elif n == 2:
    print(termoAnterior, end=' ')
    print(termoAtual, end=' ')
    exit()
elif n > 2:
    print(termoAnterior, end=' ')
    while contador < n:
        print(termoAtual, end=' ')
        termoAtual = termoAtual + termoAnterior
        termoAnterior = termoAtual - termoAnterior
        contador += 1
else:
    print('Resposta inválida, encerrando o programa!')
    exit()
