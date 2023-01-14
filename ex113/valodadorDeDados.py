#Funcao de validação de valores
def leiaDinheiro(msg): 
  válido = False
  while not válido:
    entrada = str(input(msg)).replace(',', '.').strip( )
    if entrada.isalpha() or entrada == ' ':
      válido = False
      print(f'\033[31mEntrada: \"{entrada}\" , Digite só números\033[m')
    else:
      válido = True    
      valor = float(entrada)    
  return valor
  
  