from PySimpleGUI import PySimpleGUI as sg

#Layout- BrowBlue
sg.theme('BrownBlue')
layout = [
     [sg.Text('Valor 1'),sg.Input(key='valor1', size=(15, 1))],
     [sg.Text('valor 2'),sg.Input(key='valor2', size=(15, 1))],
     [sg.Button('Comparar')]
     #[sg.Output(size=(5, 0))],
     
]

#janela
janela = sg.Window('Tela de comparar', layout)
#ler eventos
while True:
   eventos, valores = janela.read()
   if eventos == sg.WINDOW_CLOSED:
      break
   if eventos == 'Comparar':
      if valores['valor1'] > valores['valor2']:
         maior = valores['valor1']
      
      else:
         maior = valores['valor2']
      print(f'O maior valor foi {maior}')

   