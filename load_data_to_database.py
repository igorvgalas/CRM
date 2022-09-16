'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''
import sqlite3


class LoadDataToDatabase:
    '''...'''

    def __init__(self, my_list):
        self.my_list = my_list

    def clean_table_orders(self):
        '''Delete old records from table Orders'''
        with sqlite3.connect('db.sqlite3') as conn:
            delete_old_records = "DELETE FROM Orders"
            conn.execute(delete_old_records)
            conn.commit()

    def add_data_to_orders(self):
        '''Make a new records to Orders table'''
        with sqlite3.connect('db.sqlite3') as conn:
            make_records_to_orders = "INSERT INTO Orders VALUES (?,?,?,?)"
            for row in self.my_list:
                conn.execute(make_records_to_orders, list(row))
            conn.commit()

    def add_records_to_clients(self):
        '''Add and update a client data in Clients table'''
        my_new_list = []
        for rows in self.my_list:
            my_new_list.append(rows[1:3])
        with sqlite3.connect('db.sqlite3') as conn:
            make_records_to_clients = "INSERT OR IGNORE INTO Clients VALUES (Null,?,?)"
            for row in my_new_list:
                conn.execute(make_records_to_clients, list(row))
            conn.commit()
