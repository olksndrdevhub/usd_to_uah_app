import PySimpleGUI as sg


sg.theme('DarkAmber')

connecting_layout = [
    [sg.Text('Waiting to conection...')]
]
connecting_window = sg.Window('Connection...', connecting_layout)

# while True:
#     event, values = connecting_window.read()

#     if event == sg.WIN_CLOSED or event == 'Exit': 
#         break