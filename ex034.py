salario = float(input('Qual é seu salário: '))

if salario >= 1250:
   ao = salario + (salario * 10) / 100
   #print('O seu novo salário é {:.2f} R$'.format(ao1))
   
else:
   ao = salario + (salario * 15) / 100
   #print('O seu novo salário é de {:.2f} R$'.format(ao2))
print('Quem ganhava {:.2f} R$ passa a ganhar \033[1;31;36m{:.2f} R$'.format(salario, ao))