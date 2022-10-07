import mysql.connector


class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance


@Singleton
class DBConnect:

    connection = None

    def __init__(self, db):
        self.db = db

    def get_connection(self):
        if self.connection is None:
            self.connection = mysql.connector.connect(
                host="localhost", user="root", passwd="", db=self.db)
        return self.connection


class DBRecords:

    query_client = '''INSERT IGNORE INTO Clients (id, client_name, phone_number) VALUES (Null,%s,%s) '''
    query_orders = '''INSERT INTO 
        Orders (id, phone_number, appointment_date_time, service_name, pay_amount, pay_method) 
        VALUES (Null,%s,%s,%s,%s,%s) '''

    def __init__(self, client_list):
        self.client_list = client_list

    def records_client(self):
        records_client = []
        for item in self.client_list:
            records_client.append(item[0:2])
        return records_client

    def records_orders(self):
        records_orders = []
        for item in self.client_list:
            records_orders.append(item[1:])
        return records_orders


if __name__ == '__main__':

    db = DBConnect('bndatabase').get_connection()
    bc = DBConnect('bndatabase').get_connection()

    print(db)
    print(bc)
