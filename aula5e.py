d = float(input('Digite a distância da viagem km/h: '))
if d <= 200:
    p = d * 0.50
    print('Voce irá pagar {:.2f} R$ pela viagem'.format(p))
else:
    pr = d * 0.45
    print('A tua distância escedeu o limite de 200km/h agora cada km/h custa 0.45R$ ')
    print('Você irá pagar {:.2f} R$ pela viagem '.format(pr))