print('Em que periodo você estuda?')
print('Digite')
print('"M" para matutino')
print('"V" para vespertino')
print('"N" para noturno')

def checagem(periodo):
    if periodo == 'm' or periodo == 'v' or periodo == 'n':
        return True
    else:
        return False

def receptor():
    periodo = input().lower()
    if checagem(periodo) == True:
        return periodo
    else:
        print('Digite um valor válido')

    receptor()

def boasvindas(periodo):
    if periodo == 'm':
        print('Bom dia')
    elif periodo == 'v':
        print('Boa tarde')
    else:
        print('Boa noite')
    return


boasvindas(receptor())
