import PySimpleGUI as sg

from connection_window import connecting_window
from USDtoUAH import get_usd_to_uah_rate, get_converted_currency

sg.theme('DarkAmber')

rate = get_usd_to_uah_rate()

# while rate is None:
#     event, values = connecting_window.read()
# else:
#     connecting_window.close()

print(rate)


layout = [
    [sg.Text('USD to UAH  currency converter')],
    [sg.Text('If you sell USD, price will be: {} UAH per 1 USD'.format(rate))],
    [sg.Text('How much USD you want to sell?'), sg.InputText(size=(15,1))],
    [sg.Button('Convert to UAH'), sg.Button('Exit')],
    [sg.Text('You will receive: '), sg.Text(size=(15,1), key='-UAH-'), sg.Text(' UAH!')],
    ]


# Create the Window
window = sg.Window('USDtoUAH', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit': 
        break

    if int(values[0]) >= 1:
        uah = get_converted_currency(values[0], rate)
        window['-UAH-'].update(str(uah))


window.close()