'''
Module that create connection using Singleton pattern
and makes records to database
'''
import mysql.connector


class Singleton:
    '''Class for control the connection to database by Singleton pattern.'''

    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance


@Singleton
class DBConnect:
    '''Class that provide connection to database by Singleton pattern'''

    connection = None

    def __init__(self, db):
        self.db = db

    def get_connection(self):
        '''Get connection to DataBase'''
        if self.connection is None:
            self.connection = mysql.connector.connect(
                host="localhost", user="root", passwd="", db=self.db)
        return self.connection


class DBRecords:
    '''Class of objects that make records to the data base in tables orders and clients'''

    def __init__(self, conn, client_list):
        self.client_list = client_list
        self.conn = conn

    def record_orders(self):
        '''For client in client list select record from client table 
        compare it, if exists add id to client and makes records to orders table, 
        if not before adding records to order table create new row with new client 
        in clients table
        '''
        cursor = self.conn.cursor()
        for client in self.client_list:
            cursor.execute(
                'SELECT * from clients WHERE phone_number ='+f'{client[1]}')
            check_exist = cursor.fetchone()
            if check_exist is not None:
                client.append(check_exist[0])
            if check_exist is None:
                cursor.execute(
                    'INSERT INTO clients (id, client_name, phone_number) VALUES (Null,%s,%s)', client[0:2])
                client.append(cursor.lastrowid)
            cursor.execute(
                'INSERT INTO orders (id, appointment_date_time, service_name, pay_amount, pay_method, client_id) VALUES (Null,%s,%s,%s,%s,%s)', client[2:])
        self.conn.commit()


if __name__ == '__main__':

    db = DBConnect('bndatabase').get_connection()
    bc = DBConnect('bndatabase').get_connection()

    print(db)
    print(bc)
