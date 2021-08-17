def calculomedia(p1,p2):
    media = (p1 + p2) / 2
    return float(media)


def calculoconceito(media):
    if media >= 9:
        conceito = 'A'
    elif media >= 7.5:
        conceito = 'B'
    elif media >= 6.0:
        conceito = 'C'
    elif media >= 4.0:
        conceito = 'D'
    else:
        conceito = 'E'
    
    return conceito


def calculoavaliacao(conceito):
    aprovado = ['A' , 'B' , 'C']
    if conceito in aprovado:
        return 'Aprovado'
    else:
        return 'Reprovado'
    

def receptor():
    p1 = input('Digite a nota da P1 ')
    p2 = input('Digite a nota da P2 ')
    return float(p1) , float(p2)


def imprimir(p1 , p2 , media , conceito , avaliacao):
    print('----------------------------------------')
    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))
    print('Média: {}'.format(media))
    print('Nota: {}'.format(conceito))
    print('Você foi {}.'.format(avaliacao))
    return


def main():
    notas = []
    notas = receptor()
    media = calculomedia(notas[0],notas[1])
    conceito = calculoconceito(media)
    avaliacao = calculoavaliacao(conceito)
    imprimir(notas[0],notas[1],media,conceito,avaliacao)
    return


main()