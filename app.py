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
from data.configdata import spreadsheet_url, sheet_name
from data.ReadOrderFile import ReadOrderFile
from data.Format import Format
from DBConnect import DBConnect
from sms.create_sms import create_sms
from sms.send_sms import send_sms

readOrderFile = ReadOrderFile(spreadsheet_url, sheet_name)
readOrderFile.extract_data(str(date.today() + timedelta(1)))
order_data = readOrderFile.toList()
order_list = order_data.tolist()

sms_list = Format(order_list)
client_list = sms_list.format_phone_number()

#loader = DBConnect(client_list)
# loader.make_records_client()
# loader.make_records_orders()
sms_list.format_date_time()
today_reminder = create_sms(order_list)
print(len(today_reminder))
send_sms(today_reminder)
