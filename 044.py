print('-=-=-=-=-=- LOJAS NYELTIANAS -=-=-=-=-=-')
valor = float(input('Informe o valor das compras: R$'))
opcao = int(input('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
Informe a opção desejada: '''))

if opcao == 1:
    print('Sua compra de R${:.2f} à vista ou em cheque custará R${:.2f}'.format(valor, valor*0.9))
elif opcao == 2:
    print('Sua compra de R${:.2f} à vista no cartão custará R${:.2f}'.format(valor, valor * 0.95))
elif opcao == 3:
    print('Sua compra custará R${:.2f} no cartão dividido em duas parcelas de R${:.2f}'.format(valor, valor/2))
elif opcao == 4:
    qMes = int(input('Qual a quantidade de meses? '))
    valorFinal = valor * 1.2
    print('Sua compra de R${:.2f} parcelada em {} meses custará R${:.2f} em {} parcelas de R${:.2f}'.format(valor, qMes, valorFinal, qMes, valorFinal/qMes))
else:
    print('Erro! Informe uma opção válida')