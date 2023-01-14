#COMO CRIAR E MODIFICAR ARQUIVOS: 
valores_celulares = [850, 2230, 1500, 3500, 5000]

with open('valores_celulares.txt', 'w') as arquivo:
  for valor in valores_celulares:
    arquivo.write(str(valor)+  '\n')
    