def validador(dia):
    while not dia.isdigit():
        return False
    dia = int(dia)
    if dia in range (0 , 8):
        return True
    else:
        return False

def receptordia():
    dia = input('Digite o dia númerico (1-7) da semana ')
    if validador(dia) == True:
        return int(dia)
    else:
        print('Digite um valor entre 1 e 7')
    return receptordia()

def diasdasemana(dia):
    if dia == 1:
        print('Domingo')
    elif dia == 2:
        print('Segunda')
    elif dia == 3:
        print('Terça')
    elif dia == 4:
        print('Quarta')
    elif dia == 5:
        print('Quinta')
    elif dia == 6:
        print('Sexta')
    else:
        print('Sábado')
        
def main():
    diasdasemana(receptordia())
    return

main()