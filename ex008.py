m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('O valor em km é {} \n O valor em hm é {} \n O valor em dam é {} \n O valor em dm é {:.0f} \n O valor em cm é {:.0f} \n O valor em mm é {:.0f}'.format (km, hm, dam, dm, cm, mm))