a = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))
m2 = a * l
ln = m2 / 2
print('A área de uma parede com {} m de altura e {} m de largura,{}×{}, é de {:.3f} m²,é necessário {:.3f}L para pintar a parede'.format(a, l, a, l, m2, ln))