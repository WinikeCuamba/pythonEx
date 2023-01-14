valor = float(input('Digite o preço do produto MT '))
n_valor = valor - (valor * 5 / 100)
print('Um produto que custa {:.2f}MT com desconto de 5% \n Tem o novo preço de {:.2f}MT'.format(valor, n_valor))