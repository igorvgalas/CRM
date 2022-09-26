'''
This module created by Ihor Halas for BNproject.

Functions:
   formating_phone_number -Check the phone number and formating it to International format

Variable:
    my_list - list of list with customer data that containe phone number
'''


def formating_phone_number(my_list):
    '''Check the phone number and formating it to International format'''
    for item in my_list:
        if len(str(item[1])) < 9 or len(str(item[1])) > 9:
            my_list.remove(item)
        if len(str(item[1])) == 9:
            item[1] = (f'+380{item[1]}')
    return my_list
