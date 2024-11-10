from time import sleep

def contador(inicio, fim, passo):
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo > 0:
        if inicio < fim:
            nAtual = inicio
            while nAtual <= fim:
                sleep(0.5)
                print(f'{nAtual}', end=' ')
                nAtual += passo
        elif inicio > fim:
            nAtual = inicio
            while nAtual >= fim:
                sleep(0.5)
                print(f'{nAtual}', end=' ')
                nAtual -= passo
    if passo < 0:
        nAtual = inicio
        while nAtual >= fim:
            sleep(0.5)
            print(f'{nAtual}', end=' ')
            nAtual += passo
    print('Fim!')

contador(1, 10, 1)
contador(10,0,2)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)