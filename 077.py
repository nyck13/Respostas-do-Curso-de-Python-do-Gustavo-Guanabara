palavras = ('NYELTON', 'LÁPIS', 'CANETA', 'COMPUTADOR', 'ESTETOSCÓPIO', 'ENGENHARIA', 'MINECRAFT', 'DORMIR', 'CACHORRO', 'ORGANIZAÇÃO', 'ANIMAL', 'ALFABETO')
for p in palavras:
    print(f'\n Na palavra {p.upper()} tem ', end='')
    for letra in p:
        if letra.lower() in 'aàáâãeéêiíoóuú':
            print(letra, end=' ')