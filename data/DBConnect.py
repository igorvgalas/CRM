'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''
import mysql.connector
from data.SingletonClass import SingletonClass


class DBConnect:

    __metaclass__ = SingletonClass

    def __init__(self, client_list):
        self.dbconn = mysql.connector.connect(host='localhost', user='root',
                                              passwd='', db='bndatabase')
        self.dbcurs = self.dbconn.cursor()
        self.client_list = client_list

    def __get_record(self, query):
        self.dbcurs.execute(query)
        result = self.dbcurs.fetchall()
        return result

    def __make_record(self, query, records):
        self.dbcurs.executemany(query, records)
        self.dbconn.commit()

    def make_records_client(self):
        records = []
        for item in self.client_list:
            records.append(item[0:2])
        query = '''INSERT IGNORE INTO Client (id, client_name, phone_number) VALUES (Null,%s,%s) '''
        self.__make_record(query, records)

    def make_records_orders(self):
        records = []
        for item in self.client_list:
            records.append(item[1:])
        query = '''INSERT INTO 
        Orders (id, phone_number, appointment_date_time, service_name, pay_amount, pay_method) 
        VALUES (Null,%s,%s,%s,%s,%s) '''
        self.__make_record(query, records)


if __name__ == '__main__':
    client_list = [['Леся', '+380679958106', '2022-10-07 10:00:00', 'Зн.ч.гл', 400, 'готівка'],
                   ['Ірина', '+380971177091',
                    '2022-10-07 11:30:00', 'ч.гл', 400, 'карта'],
                   ['Іванна', '+380961483952', '2022-10-07 13:00:00', 'Зн.ч.гл', 500, 'карта']]
    dc = DBConnect(client_list)
    dc.make_records_client()
    dc.make_records_orders()
