frase = str(input('Informe a frase: ')).strip()
frase = frase.replace(' ', '')
fraseInvertida = ''

for i in range(len(frase) - 1, -1, -1):
    fraseInvertida = fraseInvertida + frase[i]

if fraseInvertida == frase:
    print('A frase informada é um palindromo!')
else:
    print('A frase informada não é um palindromo!')

