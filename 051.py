print('==============================================')
print('====== GERADOR DE PROGRESSÃO ARITMÉTICA ======')
print('==============================================')

termo = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))

for i in range(0, 10):
    print('{}'.format(termo), end=' ')
    termo = termo + razao