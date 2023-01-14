from PySimpleGUI import PySimpleGUI as sg
  
c = 0 

   for c in range(1, 16):
       layout = [
                [sg.Button("Hacker", size=(15, 10))]
          ]
       layout2 = [
                [sg.Button("Hacker1", size=(15, 10))]
          ]
          
       janela = sg.Window(f'Janela Hacker {c}', layout)
       janela2 = sg.Window('Janela Hacker ', layout2)
       while True:
          events, values = janela.read()
          if events == sg.WINDOW_CLOSED:
               break
              
          if events == 'Hacker':
               for c in range(1, 10):
                 c += 1
                 while True:
                     eventos, valores = janela2.read()
                     if eventos == sg.WINDOW_CLOSED:
                          break    
                                 
                            
                                    janelas()        