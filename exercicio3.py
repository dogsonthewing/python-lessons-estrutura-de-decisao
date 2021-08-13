def checagem():
    sexo = str.lower(str(input('Digite seu sexo: ')))

    if sexo == 'm':
        print('Sexo masculino')
    elif sexo == 'f':
        print('Sexo feminino')
    else:
        print('Inválido, tente novamente')
        checagem()
    return

checagem()


