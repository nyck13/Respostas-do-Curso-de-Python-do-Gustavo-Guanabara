print('==============================================')
print('====== GERADOR DE PROGRESSÃO ARITMÉTICA ======')
print('==============================================')

termo = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))
contador = 0

while contador < 10:
    print('{}'.format(termo), end=' ')
    termo = termo + razao
    contador += 1