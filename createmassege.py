'''
This module created by Ihor Halas for BNproject.

Classes:
   

Functions:
   

Variable:
    
'''


def create_massage(order_list):
    '''Create messages from given list'''
    today_sms = {}
    for name, phone_number, date_time, servise in order_list:
        massage = f'''Доброго дня {name}. Нагадуємо {date_time} у Вас запис в Beauty nails. '''
        today_sms[phone_number] = massage
    return today_sms
