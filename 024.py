cidade = str(input('Informe o nome da cidade: '))
cidade = cidade.upper()
cidade = cidade.split()
print('A cidade comça com "Santo"? {}'.format(cidade[0] == 'SANTO'))