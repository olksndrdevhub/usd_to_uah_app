import requests
from time import sleep
from connection_window import connecting_window



MONOBANK = 'https://api.monobank.ua/bank/currency'

CANT_CONNECT_TO_SERVICE_ERROR = 'CAN`T CONNECT TO SERVICE'



def get_usd_to_uah_rate():

    responce = requests.get(MONOBANK)


    while responce.status_code != 200:
        connecting_window.read(timeout=10)
        sleep(2)
        print('waiting to connect...')
        responce = requests.get(MONOBANK)
        


    else: 
        if responce.status_code == 200:
            connecting_window.close()
            print(responce.status_code)
            responce_json = responce.json()

            usd_to_uah = responce_json[0]

            rate_by = usd_to_uah.get('rateBuy')

            return rate_by
            
    return CANT_CONNECT_TO_SERVICE_ERROR

def get_converted_currency(usd, rate):

    result_uah = float(usd) * float(rate)
    uah = round(result_uah, 2)

    return uah