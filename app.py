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
   format_phone_number
   format_date_time
   add_data_to_orders
   add_records_to_clients
   create_message
   send_message

Variables:
    data_frame
    df
    my_df
    my_list
    my_list_to_orders
    today_remainds

'''
from datetime import timedelta, date
from sms.config import spreadsheet_url, sheet_name
from data.ReadFile import ReadFile
from data.OrderDataPreparer import OrderDataPreparer
from data.Format import Format
from data.LoadDataToDatabase import LoadDataToDatabase
from sms.create_sms import create_sms
from sms.send_sms import send_sms


data_frame = ReadFile(spreadsheet_url, sheet_name)
df = data_frame.read_orders_file()

my_df = OrderDataPreparer(df)
my_df.pick_data_by_date(str(date.today() + timedelta(1)))
order_list = my_df.extract_data_to_list()

sms_list = Format(order_list)
load_to_orders = LoadDataToDatabase(order_list)
sms_list.format_phone_number()
load_to_orders.add_data_to_database()
sms_list.format_date_time()

today_reminder = create_sms(order_list)

send_sms(today_reminder)
