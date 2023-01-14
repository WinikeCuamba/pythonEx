from random import choice
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input ('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
e = choice (lista)
print('O escolhido é {}'.format(e))

