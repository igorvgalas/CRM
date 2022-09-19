'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''

import requests
from config import auth_token


def send_massage(today_remaings_dict):
    '''Take dict with phone number as key and text of massage as a value,
     iterate through this dict and send post request to send massage with remainds'''
    for key,  value in today_remaings_dict.items():
        response = requests.post(
            'https://api.turbosms.ua/message/send.json',
            json={
                "recipients": [f"{key}"],
                "viber": {
                    "sender": "Mobibon",
                    "text": f"{value}"
                },
                "sms": {
                    "sender": "BEAUTY",
                    "text": f"{value}"
                }
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {auth_token}'}
        )
        return response
