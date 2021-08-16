num_a = float(input('Digite o primeiro número '))
num_b = float(input('Digite o segundo número '))
num_c = float(input('Digite o terceiro número '))

if num_a > num_b and num_a > num_c:
   print(num_a)
elif num_b > num_a and num_b > num_c:
    print(num_b)
else:
    print(num_c)
