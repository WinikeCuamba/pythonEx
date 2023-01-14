from random import randint
from time import sleep
print('=Ω=' * 14)
print('Vou pensar em um número tente adivinhar')
print('=Ω=' * 14)

num = int(input('Em que número pensei: '))
print('Processando...')
sleep (1.5)
ve = randint(0, 5)
if ve == num:
   print('Você acertou!!!, o número pensado é {}'.format(ve))
else:
   print('Você errou o número pensado é {} e não {}'.format(ve, num))
