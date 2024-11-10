print('-------------------------')
print('   CARRINHO DE COMPRAS   ')
print('-------------------------')

nome = str(input('Nome do produto: '))
preco = float(input('Preço: '))

total = 0
produtosAcima1000 = 0
nomeProdutoMaisBarato = nome
precoProdutoMaisBarato = preco

while True:
    total += preco

    if preco > 1000:
        produtosAcima1000 += 1

    resposta = str(input('Quer continuar? [S]/[N]')).strip().upper()
    if resposta == 'N':
        break

    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))

    if preco < precoProdutoMaisBarato:
        nomeProdutoMaisBarato = nome

print('''O total da compra é R${:.2f}
A quantidade de produtos acima de RS1000.00 é {}
O produto mais barato é {}'''.format(total, produtosAcima1000, nomeProdutoMaisBarato))

