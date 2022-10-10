'''
This module created by Ihor Halas for BNproject.

Functions:
create_message

Parameter:
order_list -> list with clients data
'''


def create_sms(order_list):
    '''Create messages from given list'''
    today_sms = {}
    for value in order_list:
        message = f'''{value[0]} нагадуємо у Вас запис {value[2]} Beauty nails.В разі змін повідомте на viber 0990820412'''
        #message = f'''{value[0]} запис {value[2]} Beauty nails скасовано.Звяжемося з Вами після стабілізації ситуації. Бережіть себе. '''
        phone_number = value[1]
        today_sms[message] = phone_number
    return today_sms


if __name__ == "__main__":
    ord_list = [['Ірина', '+380504316733', '11:30 01/10', 'Зн.ч.гл'],
                ['Ірина', '+380504316733', '13:00 01/10', 'брови фар'],
                ['Наталя', '+380982346789', '13:40 01/10', 'Зн.ч'],
                ['Оксана', '+380677180374', '16:00 01/10', 'Зн.ч.гл'],
                ['Вікторія', '+380975869469', '10:00 01/10', 'Зн']]
    today_mess = create_sms(ord_list)
    print(today_mess)
