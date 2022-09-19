'''
This is the app created by Ihor Halas for BNproject.
Retrieve data from xlsx file for certain date,
modify it and add needed data to database in table Orders.
After that create and send remainding message to the client.
And finally create and update a Clients table in Database.

Classes:
   ReadFile
   LoadDataToDatabase
   OrderDataPreparer

Functions:
   pick_data_by_date
   extract_data_to_list
   formating_phone_number
   clean_table_orders
   add_data_to_orders
   add_records_to_clients
   create_massage
   send_massage

Variable:
    data_frame
    df
    my_df
    my_list
    my_list_of_orders
    today_remainds

'''

from order_data_preparer import OrderDataPreparer
from read_file import ReadFile
from formating_phone_number import formating_phone_number
from load_data_to_database import LoadDataToDatabase
from createmassege import create_massage
from send import send_massage

CURRENT_DATE = '2022-10-01'  # curr_date = pd.to_datetime('today').date()
FILE_NAME = 'October.xlsx'
SHEET_NAME = 'October'

#CURRENT_DATE = input('Enter the date please:')
#FILE_NAME = input('Please add a xlsx file path:')
#SHEET_NAME = input('Sheet name:')

data_frame = ReadFile()
df = data_frame.read_orders_file(FILE_NAME, SHEET_NAME)

my_df = OrderDataPreparer(df)
my_df.pick_data_by_date(CURRENT_DATE)
my_df.extract_data_to_list()

my_list = formating_phone_number(my_df.data_frame)

my_list_of_orders = LoadDataToDatabase(my_list)
my_list_of_orders.clean_table_orders()
my_list_of_orders.add_data_to_orders()
my_list_of_orders.add_records_to_clients()

today_remainds = create_massage(my_list)
send_massage(today_remainds)
