def leiaMoeda(texto = ''):
    while True:
        resposta = str(input(f'{texto}')).replace(',', '.')
        if resposta.isalpha() or resposta.strip() == '':
            print('Resposta inválida!')
        else:
            return float(resposta)