def aumentar(valor = 0, aumento = 0):
    return valor*((100+aumento)/100)

def diminuir(valor = 0, dimuicao = 0):
    return valor*((100-dimuicao)/100)

def dobrar(valor = 0):
    return valor*2

def metade(valor = 0):
    return valor/2

def formatar(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')