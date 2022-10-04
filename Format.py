'''
This module created by Ihor Halas for BNproject.

Functions:
   formating_phone_number -Check the phone number and formating it to International format

Variable:
    my_list - list of list with customer data that containe phone number
'''
from datetime import datetime


class Format:

    def __init__(self, my_list):
        self.my_list = my_list

    def format_phone_number(self):
        '''Check the phone number and formating it to International format'''
        for item in self.my_list:
            if len(str(item[1])) < 9 or len(str(item[1])) > 9:
                self.my_list.remove(item)
                print('One or more phone number are not correct')
            if len(str(item[1])) == 9:
                item[1] = (f'+380{item[1]}')
        return self.my_list

    def format_date_time(self):
        '''Format date time to make it shorter for sms sending'''
        for item in self.my_list:
            item[2] = datetime.strptime(item[2], '%Y-%m-%d %H:%M:%S')
            item[2] = datetime.strftime(item[2], "%H:%M %d/%m")
        return self.my_list


if __name__ == "__main__":
    m_list = [['Ірина', 504316733, '2022-10-01 11:30:00', 'Зн.ч.гл'],
              ['Ірина', 504316733, '2022-10-01 13:00:00', 'брови фар'],
              ['Наталя', 982346789, '2022-10-01 13:40:00', 'Зн.ч'],
              ['Оксана', 677180374, '2022-10-01 16:00:00', 'Зн.ч.гл'],
              ['Вікторія', 975869469, '2022-10-01 10:00:00', 'Зн']]
    my_formating_list = Format(m_list)
    my_formating_list.format_phone_number()
    my_formating_list.format_date_time()
    print(m_list)
