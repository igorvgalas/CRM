'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''
import mysql.connector
from app import order_list
from data.Format import Format

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bndatabase")
my_cursor = mydb.cursor()

#sqlorders = "INSERT INTO users (name,email,age) VALUES (%s,%s,%s)"


#my_cursor.executemany(sqlStuff, records)
# mydb.commit()
