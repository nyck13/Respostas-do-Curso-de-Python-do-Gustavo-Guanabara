brasileirao = 'Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional', 'São Paulo', 'Bahia', 'Cruzeiro', 'Vasco', 'Atlético-MG', 'Grêmio', 'Criciúma', 'Fluminense', 'Vitória', 'Corinthians', 'Athletico-PR', 'Bragantino', 'Juventude', 'Cuiabá', 'Atlético-GO'

print('Os cinco primeiros colocados são: ')
for i in range(0, 5):
    print('{} - {}'.format(i + 1, brasileirao[i]))

print('Os quatro últimos colocados são: ')
for i in range(0, 4):
    print('{} - {}'.format(i + 17, brasileirao[i+16]))

print('Os times em ordem alfabética são: ')
print(sorted(brasileirao))

print('O flamengo está na posição {}'.format(brasileirao.index('Flamengo') + 1))