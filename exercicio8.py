produtos = []

produtos.append(int(input('Digite o primeiro produto ')))
produtos.append(int(input('Digite o segundo produto ')))
produtos.append(int(input('Digite o terceiro produto ')))

produto_barato = min(produtos)

print(produto_barato)