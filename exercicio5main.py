import exercicio5funcoes as fc

def main():
    p1nota = fc.receptornota('P1')
    p2nota = fc.receptornota('P2')

    mediasem = fc.calculomedia(p1nota,p2nota)

    fc.aprovacao(mediasem)
    return

main()