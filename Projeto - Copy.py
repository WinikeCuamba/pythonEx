d = int(input('Em que dia estamos: '))
print('-' * 42)
df = 31 - d
if df == 1:
    print('Falta {} dia para o aniversário do kwame '.format(df))
elif df > 1:
    print('Faltam {} dias para o aniversário do kwame '.format(df))
elif df == 0:
    print('Parabens Kwame!!!')    
dt = 11 - d
if dt == 1:
    print('Falta {} dia para começar os testes '.format(dt))
elif dt > 1:
    print('Faltam {} dias para começar os testes '.format (dt))
else:
    print(' {} Desde o dia do começo dos testes '.format(dt))
    
dtt = 18 - d
if dtt == 1:
    print('Falta {} dia para terminar os testes'.format(dtt))
elif dtt > 1:
    print('Faltam {} dias para terminar os testes '.format(dtt))
else:
    print('{} Desde o término dos testes'.format (dtt))
    
print('-' * 42)