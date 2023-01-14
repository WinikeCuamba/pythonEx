'''no = str(input('Digite o teu nome: '))
if no == 'Winike':
    print('Que nome lindo você tem! ')
else:
    print ('Que nome tão normal ')
print('Bom dia , {} !'.format(no))'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m <= 6:
    print('Estude mais da próxima ')
else:
    print('Parabens !!!')
print('A sua média é {:.2f} '.format(m))    