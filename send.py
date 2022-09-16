'''
This module created by Ihor Halas for BNproject.

Classes:
   

Functions:
   

Variable:
    
'''

from twilio.rest import Client
import createmassege
import config

ACCOUNT_SID = config.account_sid
AUTH_TOKEN = config.auth_token

client = Client(ACCOUNT_SID, AUTH_TOKEN)
for key,  value in createmassege.today_sms.items():
    massage_body = f"{value}"
    massage_to = f"+{key}"
    mass = client.messages \
        .create(
            body=massage_body,
            from_=config.from_,
            to=massage_to)
