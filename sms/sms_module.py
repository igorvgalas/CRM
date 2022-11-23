'''
This module created by Ihor Halas for BNproject.

It's make http request to post data for Turbo sms servise for 
sending a remainds messades for clients appointment

Functions:
send_message

Variable:
today_remaings_dict -> containe message and phone number for every appointment.

'''

import requests
#from sms.config import auth_token


def create_sms(order_list):
    '''Create messages from given list'''
    today_sms = {f'{value[0]} нагадуємо у Вас запис {value[2]} Beauty nails.В разі змін повідомте на viber 0990820412': value[1]
                 for value in order_list}
    print(today_sms)
    return today_sms


def create_sms_to_all(client_list):
    today_sms = {}
    for value in client_list:
        today_sms[value[1]] = f'{value[0]} у нас немає перебоїв зі світлом,працюємо в звичному режимі!Є перебої зі звязком,записуватися краще через viber 0990820412.'
    return today_sms


def send_sms(today_remaings_dict):
    '''This method takes dictionary with phone number as value and text of massage as a key,
     iterates through this dictionary sends post request using TurboSMS API.
     After that TurboSMS sends a reminder sms to clients'''
    for key,  value in today_remaings_dict.items():
        response = requests.post(
            'https://api.turbosms.ua/message/send.json', timeout=10,
            json={
                "recipients": [f"{key}"],
                "sms": {
                    "sender": "BeautyNails",
                    "text": f"{value}"
                }
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {auth_token}'}
        )


if __name__ == "__main__":
    ord_list = [['Ірина', '+380504316733', '11:30 01/10', 'Зн.ч.гл'], ]
    today_mess = create_sms(ord_list)
    print(today_mess)
