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
from config import auth_token


def send_message(today_remaings_dict):
    '''Take dict with phone number as key and text of massage as a value,
     iterate through this dict and send post request to send massage with remainds'''
    for key,  value in today_remaings_dict.items():
        response = requests.post(
            'https://api.turbosms.ua/message/send.json',
            json={
                "recipients": [f"{value}"],
                "viber": {
                    "sender": "Mobibon",
                    "text": f"{key}"
                },
                "sms": {
                    "sender": "BEAUTY",
                    "text": f"{key}"
                }
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {auth_token}'}
        )
        return response


def main() -> None:
    print('Remaind message was sent successfully')


if __name__ == "__main__":
    main()
