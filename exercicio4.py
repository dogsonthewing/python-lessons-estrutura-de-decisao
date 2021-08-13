vogais = ['a' , 'e' , 'i' , 'o' , 'u']

letra = str.lower(str(input('Digite uma letra: ')))

if letra in vogais:
    print('É uma vogal')
else:
    print('Não é uma vogal')