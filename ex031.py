from time import sleep
di = float(input('Qual é a distância da tua viagem em km: '))
print('Você ira começar uma viagem de{}km'.format(di))
print('Processando...')
sleep(0.5)


'''if di <= 200:
   print('Você ira pagar {:.2f} R$ pela viagem'.format(di * 0.50))
else:
   print('Você escedeu o limite de 200km/h agora cada km custa 0.45 R$')
   print('Você ira pagar {:.2f} R$ pela viagem'.format(di * 0.45))'''

   
preço = di * 0.50 if di <= 200 else di * 0.45  
print('Preço da passagem será de {:.2f} R$'.format(preço))