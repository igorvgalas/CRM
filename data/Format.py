'''
This module created by Ihor Halas for BNproject.

Functions:
   formating_phone_number -Check the phone number and formating it to International format
   format_date_time - return date time in "H:M d/m" format.
Variable:
    my_list - list of list with customer data that containe phone number
'''
from datetime import datetime


class InvalidValueError(Exception):
    '''Error with phone number format'''


class Format():
    '''Format list of orders data'''

    def __init__(self, my_list: list):
        self.my_list = my_list

    def format_phone_number(self):
        '''Formar order list before sending sms'''
        self.__del_incorrects()
        self.__add_code_to_phone_number()

    def format_date_time(self):
        '''Format date time to make it shorter for sms sending'''
        for item in self.my_list:
            item[2] = datetime.strptime(item[2], '%Y-%m-%d %H:%M:%S')
            item[2] = datetime.strftime(item[2], "%H:%M %d/%m")
        return self.my_list

    def __del_incorrects(self):
        try:
            for item in self.my_list:
                if len(str(item[1])) != 9:
                    self.my_list.remove(item)
        except IndentationError:
            print('One or more phone numbers had an error')

    def __add_code_to_phone_number(self):
        '''Check the phone number and formating it to International format'''
        for item in self.my_list:
            item[1] = (f'+380{item[1]}')
        return self.my_list


if __name__ == "__main__":
    # m_list example of my_list that we get for our class
    m_list = [['Ірина', 504316735, '2022-10-01 11:30:00', 'Зн.ч.гл'],
              ['Оксана', 677, '2022-10-01 16:00:00', 'Зн.ч.гл'],
              ['Вікторія', 975869466, '2022-10-01 10:00:00', 'Зн'],
              ['Вікторія', 975869, '2022-10-01 10:00:00', 'Зн']]
    my_formating_list = Format(m_list)
    my_formating_list.format_phone_number()
    my_formating_list.format_date_time()
    print(m_list)
