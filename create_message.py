'''
This module created by Ihor Halas for BNproject.

Classes:
   

Functions:
   

Variable:
    
'''


def create_message(order_list):
    '''Create messages from given list'''
    today_sms = {}
    for value in order_list:
        message = f'''Доброго дня {value[0]}. Нагадуємо {value[2]} у Вас запис в Beauty nails. '''
        phone_number = value[1]
        today_sms[message] = phone_number
    return today_sms
