numeros = []

numeros.append(int(input('Digite o primeiro número ')))
numeros.append(int(input('Digite o segundo número ')))
numeros.append(int(input('Digite o terceiro número ')))

numeros = sorted(numeros, reverse = True)

for x in range(len(numeros)):
    print(numeros[x])