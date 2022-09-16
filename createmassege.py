'''
This module created by Ihor Halas for BNproject.

Classes:
   

Functions:
   

Variable:
    
'''

import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    cursor = conn.execute("SELECT * FROM Orders")
    my_list = cursor.fetchall()


today_sms = {}
for date_time, name, phone_number, servise in my_list:
    massage = f'''Доброго дня {name}. {date_time} Ви записані на {servise}. Чекаємо вас з нетерпінням.'''
    today_sms[phone_number] = massage
print(today_sms)
