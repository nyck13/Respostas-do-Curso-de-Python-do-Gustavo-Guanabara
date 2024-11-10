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