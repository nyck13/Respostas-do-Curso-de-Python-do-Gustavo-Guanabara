print('==============================================')
print('====== GERADOR DE PROGRESSÃO ARITMÉTICA ======')
print('==============================================')

termo = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))
contador = 0
termoTotais = 0
resposta = 1

while contador < 10:
    print('{}'.format(termo), end=' ')
    termo = termo + razao
    contador += 1
    termoTotais += 1

print('')
resposta = int(input('Quantos termos você quer ver mais? '))

while resposta != 0:
    termoTotais = termoTotais + resposta
    while contador < termoTotais:
        print('{}'.format(termo), end=' ')
        termo = termo + razao
        contador += 1
    print('')
    resposta = int(input('Quantos termos você quer ver mais? '))
print('Programa encerrado! ')