'''from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = sqrt(co ** 2 + ca ** 2) 
print('O valor da hipotenusa é {:.2f} '.format(hi))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor de cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é de {:.2f}'.format (hi))