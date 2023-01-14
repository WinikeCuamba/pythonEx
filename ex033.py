
num = int(input('Digite um número:'))
n1 = int(input('Digite outro número:'))
n2 = int(input('Digite outro número:'))
#Verificando quem é o maior número
maior = num
if n2 > num and n2 > n1:
   maior = n2 
if n1 > num and n1 > n2:
   maior = n1
print('O maior número é {}'.format(maior))
#Verificando quem é o menor número
menor = num
if n1 < num and n1 < n2:
   menor = n1
if n2 < num and n2 < n1:
   menor = n2
print('O menor número é {}'.format(menor))