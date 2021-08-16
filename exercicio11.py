import math

def calculoreajuste(salario):
    if salario <= 280:
        ajuste_salario = salario * 0.2
        percentual_ajuste = '20%'
    elif salario in range(279 , 701):
        ajuste_salario = salario * 0.15
        percentual_ajuste = '15%'
    elif salario in range(699 , 1501):
        ajuste_salario = salario * 0.10
        percentual_ajuste = '10%'
    else:
        ajuste_salario = salario * 0.05
        percentual_ajuste = '5%'

    salario_ajustado = salario + ajuste_salario

    return math.ceil(salario), percentual_ajuste, math.ceil(ajuste_salario), math.ceil(salario_ajustado)

salario = int(input('Digite seu salário '))
salario = calculoreajuste(salario)
print('O salário original de R${} recebe o ajuste de {} equivalente a {} do valor original, totalizando em R${}.' .format(salario[0],salario[2],salario[1],salario[3]))

