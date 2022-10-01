'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''
import sqlite3


class LoadDataToDatabase:
    '''Class of conections to the database'''

    def __init__(self, my_list):
        self.my_list = my_list

    def add_data_to_database(self):
        '''Make a new records to Orders table'''
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            for row in self.my_list:
                cursor.execute(
                    ("INSERT INTO Orders VALUES (Null,?,?,?,?)"), list(row))
            cursor.execute('''INSERT OR IGNORE INTO Clients (OrderID,ClientName, PhoneNumber)
                                         SELECT OrderID, ClientName, PhoneNumber
                                         FROM
                                         (SELECT *
                                         from Orders
                                         GROUP BY PhoneNumber)
                                         ORDER BY OrderID''')

        conn.commit()
