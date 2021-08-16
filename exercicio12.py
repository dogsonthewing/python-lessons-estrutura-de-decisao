import math

def calcularsalario():
    horas_trabalhadas = int(input('Digite o suas horas trabalhadas '))
    horas_valor = int(input('Digite as horas trabalhadas '))
    salario_bruto = horas_trabalhadas * horas_valor
    return horas_trabalhadas , horas_valor , salario_bruto


def calculofgts(salario_bruto):
    valor_fgts = salario_bruto * 0.11
    return int(valor_fgts)


def calculosalarioliquido(salario_bruto):
    if salario_bruto <= 900:
        ajuste_ir = salario_bruto
        ajuste_ir_percentual = '0%'
    elif salario_bruto in range(900 , 1501):
        ajuste_ir = salario_bruto * 0.05
        ajuste_ir_percentual = '5%'
    elif salario_bruto in range(1500 , 2501):
        ajuste_ir = salario_bruto * 0.10
        ajuste_ir_percentual = '10%'
    else:
        ajuste_ir = salario_bruto * 0.20
        ajuste_ir_percentual = '20%'

    desconto_inss = salario_bruto * 0.10
    desconto_total = ajuste_ir + desconto_inss
    salario_liquido = salario_bruto - desconto_total

    return ajuste_ir_percentual, math.ceil(ajuste_ir), math.ceil(desconto_inss), math.ceil(desconto_total) , math.ceil(salario_liquido)


def imprimirtela(horas_trabalhadas , horas_valor , salario_bruto , ajuste_ir_percentual , ajuste_ir , desconto_inss , desconto_total , salario_liquido):
    print('Salário bruto ({} * {}) : R${}'.format(horas_trabalhadas,horas_valor,salario_bruto))
    print('(-) IR ({}) : R${}'.format(ajuste_ir_percentual,ajuste_ir))
    print('(-) INSS (10%) : R${}'.format(desconto_inss))
    print('FGTS (11%) : R${}'.format(calculofgts(salario_bruto)))
    print('Total de descontos : R${}'.format(desconto_total))
    print('Salário liquido : R${}'.format(salario_liquido))
    return

def main():
    salario_bruto_horas = []
    salario_liquido_descontos = []
    salario_bruto_horas = calcularsalario()
    salario_liquido_descontos = calculosalarioliquido(salario_bruto_horas[2])
    imprimirtela(salario_bruto_horas[0],salario_bruto_horas[1],salario_bruto_horas[2],salario_liquido_descontos[0],salario_liquido_descontos[1],salario_liquido_descontos[2],salario_liquido_descontos[3],salario_liquido_descontos[4])
    return

main()