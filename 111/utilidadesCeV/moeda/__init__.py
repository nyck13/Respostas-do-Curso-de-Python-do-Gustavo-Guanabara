def formatar(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def aumentar(valor = 0, aumento = 0, formatacao = False):
    res = valor*((100+aumento)/100)
    return res if formatacao is False else formatar(res)

def diminuir(valor = 0, dimuicao = 0, formatacao = False):
    res = valor*((100-dimuicao)/100)
    return res if formatacao is False else formatar(res)

def dobrar(valor = 0, formatacao = False):
    res = valor*2
    return res if formatacao is False else formatar(res)

def metade(valor = 0, formatacao = False):
    res = valor/2
    return res if formatacao is False else formatar(res)

def resumo(valor = 0, aumento = 0, diminuicao = 0):
    print('=====================================')
    print('           RESUMO DO VALOR           ')
    print('=====================================')
    print(f'Preço analisado:          {formatar(valor)}')
    print(f'Dobro do preço:           {dobrar(valor, True)}')
    print(f'Metade do preço:          {metade(valor, True)}')
    print(f'{aumento:2}% de aumento:           {aumentar(valor, aumento, True)}')
    print(f'{diminuicao:2}% de redução:           {diminuir(valor, diminuicao, True)}')