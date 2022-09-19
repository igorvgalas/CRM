'''
This module created by Ihor Halas for BNproject.

Classes:
   

Functions:
   

Variable:
    
'''


def create_massage(order_list):
    today_sms = {}
    for date_time, name, phone_number, servise in order_list:
        massage = f'''Доброго дня {name}. {date_time} Ви записані на {servise}. Чекаємо вас з нетерпінням.'''
        today_sms[phone_number] = massage
    return today_sms
