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
   pick_up_date
   extract_data_to_list
   formating_phone_number
   add_data_to_orders
   add_records_to_clients
   create_message
   send_message

Variables:
    data_frame
    df
    my_df
    my_list
    my_list_of_orders
    today_remainds

'''
from datetime import timedelta, date
from config import spreadsheet_url, sheet_name
from read_file import ReadFile
from order_data_preparer import OrderDataPreparer
from formating_order_list import formating_phone_number, format_date_time
from load_data_to_database import LoadDataToDatabase
from create_sms import create_sms
from send_sms import send_sms


data_frame = ReadFile()
df = data_frame.read_orders_file(spreadsheet_url, sheet_name)

my_df = OrderDataPreparer(df)
my_df.pick_data_by_date(str(date.today() + timedelta(1)))
my_df.extract_data_to_list()

#my_list_of_orders = LoadDataToDatabase(my_list)
# my_list_of_orders.add_data_to_database()

my_list = formating_phone_number(my_df.data_frame)
my_list = format_date_time(my_df.data_frame)
today_remainds = create_sms(my_list)
# send_sms(today_remainds)
print(today_remainds)
