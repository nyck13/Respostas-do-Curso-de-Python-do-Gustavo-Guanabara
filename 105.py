def lista(*numeros, situacao = False):
    dic = {
        'quantidadeNotas':len(numeros),
        'maiorNota':max(numeros),
        'menorNota':min(numeros),
        'media':sum(numeros)/len(numeros)
    }

    if situacao:
        if dic['media'] >= 7:
            dic['situacao'] = 'BOA'
        elif dic['media'] >= 5:
            dic['situacao'] = 'INTERMEDIÁRIA'
        else:
            dic['situacao'] = 'RUIM'

    return dic

resposta = lista(3,2,1, situacao=True)
print(resposta)
