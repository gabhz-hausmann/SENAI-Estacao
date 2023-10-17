# Não fiz bem detalhado!!
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))

if mes >= 1 and mes <= 3:
    print('Verão')
elif mes > 3 and mes <= 6:
    print('Outono')
elif mes > 6 and mes <= 9:
    print('Inverno')
elif mes == 12:
    print('Verão')
else:
    print('Primavera')