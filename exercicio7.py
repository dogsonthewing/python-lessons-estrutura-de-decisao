num_a = int(input('Digite o primeiro número '))
num_b = int(input('Digite o segundo número '))
num_c = int(input('Digite o terceiro número '))

if num_a > num_b and num_a > num_c:
   maior_numero = num_a
elif num_b > num_a and num_b > num_c:
   maior_numero = num_b
else:
    maior_numero = num_c

if num_a < num_b and num_a < num_c:
   menor_numero = num_a
elif num_b < num_a and num_b < num_c:
   menor_numero = num_b
else:
    menor_numero = num_c

print('O maior e menor numero são, respectivamente, {} e {}.' .format(str(maior_numero) , str(menor_numero)))
