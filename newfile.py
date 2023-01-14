from PySimpleGUI import PySimpleGUI as sg

sg.theme('dark') 
layout1 = [
   [sg.Text('LOJA WINIKE'.center(35),size=(20,1))],
   [sg.Text('Energia', size=(12, 1)), sg.Button('Opção 1')],
   [sg.Text('GOTV', size=(12, 1)), sg.Button('Opção 2')],
   [sg.Text('Cambio', size=(12, 1)), sg.Button('Opção 3')]
] 

janela = sg.Window('Loja', layout1)
while True:
   events, values = janela.read()
   if events == sg.WINDOW_CLOSED:
      break 
      
   if events == 'Opção 1':
      #janela.close()
      layout2 = [
         [sg.Text('Opções de energia'.center(36), size=(20, 1))],
         [sg.Button('1', size=(1, 2)), sg.Text('Quanto custa a energia?', size=(20, 2))],
         [sg.Button('2', size=(1, 2)), sg.Text('Quantos meticais são precisos para comprar energia X', size=(20, 3))],
         [sg.Button('VOLTAR')]
      ]
      
      janela2 = sg.Window('Loja', layout2)
      while True:
         events, values = janela2.read()
         if events == sg.WINDOW_CLOSED:
            break
         if events == 'VOlTAR':
            break
   
      