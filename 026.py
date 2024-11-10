frase = str(input('Qual é a sua frase? ')).upper()
print('A quantidade de vezes que aparece a letra A é de {}'.format(frase.count('A')))
print('A posição em que a letra A aparece pela primeira vez é {}'.format(frase.find('A') + 1))
print('A posição em que a letra A aparece pela úlrima vez é {}'.format(frase.rfind('A') + 1))