from time import sleep
opção = 0
while True:
   print('''-----LOJA WINIKE----
   [ 1 ] Energia
   [ 2 ] GOTV
   [ 3 ] Cambio
   [ 4 ] Sair''')
   opção = int(input('Qual é a sua opção: '))
   print('PROCESSANDO...')
   sleep(1.0)
   
   if opção == 1:
       print('''---Opções de energia
       [ 1 ] Quanto custa a energia
       [ 2 ] Quantos MT são necessários para comprar energia x ''')
       opção_energia = int(input('Qual é a sua opção: '))
              
       if opção_energia == 1:
          print('Energia custa 8.44 MT')
       if opção_energia == 2:
         num = int(input('Quantos kWh queres comprar? '))
         preço = num * 8.44
         print('{} kWh custam {} MT'.format(num, preço))
   
   elif opção == 2:
       print('''---OPOÇÕES DA GOTV---
       [ 1 ] Quanto custa o pacote essencial? 
       [ 2 ] Quanto custa o pacote plus 
       [ 3 ] Quanto custa o pacote Max''')

       opção_gotv = int(input('Qual é a sua opção? '))
       if opção_gotv == 1:
          print('O preço do pacote essencial é de 200MT')
       if opção_gotv == 2:
          print('O preço do pacote plus é de 500MT')
       if opção_gotv == 3:
          print('O preço do pacote Max é de 900')
       else:
          opção_gotv = int(input('OPÇÃO INVALIDA.DIGITE NOVAMENTE: '))
       
       
   elif opção == 3:
       print('''---OPOÇÕES DE CAMBIO---
       [ 1 ] DE METICAL PARA DOLAR
       [ 2 ] DE DOLAR PARA METICAL 
       [ 3 ] DE RANDES PARA METICAL
       [ 4 ] DE METICAL PARA RANDES''')
       opção_canbio = int(input('Qual é a sua opção: '))

       if opção_canbio == 1:
          print('1 metical está  0.016 em dolar')
          m = float(input('Quantos meticais queres cambiar: '))
          m_d = m * 0.016
          print('{:.2f}MT em dólares são {:.2f}U$S'.format(m, m_d))

       elif opção_canbio == 2:
          print('1 dólar está 63.83')
          d = float(input('Quantos dólares queres cambiar: '))
          d_m = d * 63.83
          print('{:.2f}U$S em meticais são {:.2f}MT'.format(d, d_m))

       elif opção_canbio == 3:
          print('1 rande está 3.79 meticais')
          r = float(input('Quantos randes queres cambiar: '))
          r_m = r * 3.79
          print('{}ZAR em mentical são {}MT'.format(r, r_m))

       elif opção_canbio == 4:
          print('1 Metical está 0.26 randes ')
          m = float(input('Quantos meticais queres cambiar: '))
          m_r = m * 0.26
          print('{}MT em randes são {}ZAR'.format(m, m_r))
   elif opção == 4:
      print('OBRIGADO VOLTE SEMPRE')
      break          
   else:
       opção = int(input('OPÇÃO INVALIDA. TENTE NOVAMENTE'))