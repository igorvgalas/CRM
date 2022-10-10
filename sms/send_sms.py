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
from sms.config import auth_token


def send_sms(today_remaings_dict):
    '''This method takes dictionary with phone number as value and text of massage as a key,
     iterates through this dictionary sends post request using TurboSMS API.
     After that TurboSMS sends a reminder sms to clients'''
    for key,  value in today_remaings_dict.items():
        response = requests.post(
            'https://api.turbosms.ua/message/send.json', timeout=10,
            json={
                "recipients": [f"{value}"],
                # "viber": {
                # "sender": "Mobibon",
                # "text": f"{key}"
                # },
                "sms": {
                    "sender": "BEAUTY",
                    "text": f"{key}"
                }
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {auth_token}'}
        )
