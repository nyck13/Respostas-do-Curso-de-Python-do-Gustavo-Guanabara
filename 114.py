import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro ao tentar acessar o site!')
else:
    print('Tudo OK! O site está acessível.')