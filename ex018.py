import math
an = float(input('Digite o número de um ângulo: '))
se = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de de {:.2f}'.format (an, se))
co = math.cos(math.radians(an ))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, co))
ta = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, ta))