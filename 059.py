n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))

opcao = int(input('''MENU DE AÇÕES
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Informe qual será a ação desejada: '''))

while opcao != 5:
    if opcao == 1:
        print('O resultado da soma entre {} e {} é de {}'.format(n1, n2, n1 + n2))
        opcao = int(input('Informe qual será a próxima ação: '))
    elif opcao == 2:
        print('O resultado da multiplicação entre {} e {} é de {}'.format(n1, n2, n1 * n2))
        opcao = int(input('Informe qual será a próxima ação: '))
    elif opcao == 3:
        if n1 == n2:
            print('Os dois valores {} e {} são iguais!'.format(n1, n2))
        elif n1 > n2:
            print('O primeiro valor {} é maior que o segundo valor {}'.format(n1, n2))
        else:
            print('O segundo valor {} é maior que o primeiro valor {}'.format(n2, n1))
        opcao = int(input('Informe qual será a próxima ação: '))
    elif opcao == 4:
        print('Informe quais serão os novos valores')
        n1 = float(input('Informe o primeiro valor: '))
        n2 = float(input('Informe o segundo valor: '))
        opcao = int(input('Informe qual será a próxima ação: '))
    else:
        if opcao != 0:
            print('Opção inválida!')
            opcao = int(input('Informe qual será a próxima ação: '))
        else:
            break
print('Programa encerrado!')