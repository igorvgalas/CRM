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

    def __init__(self, conn, client_list):
        self.client_list = client_list
        self.conn = conn

    def records_orders(self):
        cursor = self.conn.cursor()
        for client in self.client_list:
            cursor.execute(
                'SELECT * from Clients WHERE phone_number ='+f'{client[1]}')
            check_exist = cursor.fetchone()
            if check_exist is not None:
                client.append(check_exist[0])
            if check_exist is None:
                cursor.execute(
                    'INSERT INTO Clients (id, client_name, phone_number) VALUES (Null,%s,%s)', client[0:2])
                cursor.execute(
                    'SELECT * FROM Clients WHERE phone_number =' + f'{client[1]}')
                created_client = cursor.fetchone()
                client.append(created_client[0])
            cursor.execute(
                'INSERT INTO Orders (id, appointment_date_time, service_name, pay_amount, pay_method, client_id) VALUES (Null,%s,%s,%s,%s,%s)', client[2:])
        self.conn.commit()


if __name__ == '__main__':

    db = DBConnect('bndatabase').get_connection()
    bc = DBConnect('bndatabase').get_connection()

    print(db)
    print(bc)
