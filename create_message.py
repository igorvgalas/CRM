'''
This module created by Ihor Halas for BNproject.

Functions:
create_message    

Parameter:
order_list -> list with clients data    
'''


def create_message(order_list):
    '''Create messages from given list'''
    today_sms = {}
    for value in order_list:
        message = f'''{value[0]} хочемо нагадати {value[2]} у Вас запис в Beauty nails. В разі змін повідомте нас. До зустрічі.'''
        phone_number = value[1]
        today_sms[message] = phone_number
    return today_sms


if __name__ == "__main__":
    ord_list = [['Ірина', '+380504316733', '2022-10-01 11:30:00', 'Зн.ч.гл'],
                ['Ірина', '+380504316733', '2022-10-01 13:00:00', 'брови фар'],
                ['Наталя', '+380982346789', '2022-10-01 13:40:00', 'Зн.ч'],
                ['Оксана', '+380677180374', '2022-10-01 16:00:00', 'Зн.ч.гл'],
                ['Вікторія', '+380975869469', '2022-10-01 10:00:00', 'Зн']]
    today_mess = create_message(ord_list)
    print(today_mess)
