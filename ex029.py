velocidade = float(input('Digite a velocidade do carro: '))
if velocidade < 80:
   print('Boa viagem!!!')
   print('Limite de velocidade de 80km/h ultrapassado')
   multa = (velocidade - 80) * 7#A resposta dos maiores problemas do Homem são encontradas  momentos de lazer
   print('A tua multa é de {:.2f}'.format(multa))