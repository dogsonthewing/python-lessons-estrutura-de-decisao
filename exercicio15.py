def receptor():
    print('Informe os valores dos lados do triangulo')
    lado_ab = int(input('Digite o valor do lado AB '))
    lado_bc = int(input('Digite o valor do lado BC '))
    lado_ca = int(input('Digite o valor do lado CA '))
    return lado_ab , lado_bc , lado_ca

def detectortipo(ab,bc,ca):
    if ab == bc and ab == ca:
        print('Equilatero')
    elif ab != bc and ab != ca:
        print('Escaleno')
    else:
        print('Isóceles')
    return

def main():
    triangulo = receptor()
    detectortipo(triangulo[0],triangulo[1],triangulo[2])
    return

main()