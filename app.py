'''
This is the app created by Ihor Halas for BNproject.
Retrieve data from xlsx file for certain date,
modify it and add needed data to database in table Orders.
After that create and send remainding message to the client.
And finally create and update a Clients table in Database.

'''
from datetime import timedelta, date
from data.configdata import spreadsheet_url, sheet_name, database_name
from data.read_order_file import ReadOrderFile
from data.format import Format
from data.db_connector import DBConnect, DBRecords
from sms.create_sms import create_sms
from sms.send_sms import send_sms

read_order_file = ReadOrderFile(spreadsheet_url, sheet_name)
read_order_file.extract_data(str(date.today() + timedelta(0)))
order_list = read_order_file.toArray().tolist()

sms_list = Format(order_list)
client_list = sms_list.format_phone_number()

conn = DBConnect(database_name).get_connection()

recorder = DBRecords(conn, client_list)
recorder.record_orders()

# sms_list.format_date_time()
#today_reminder = create_sms(client_list)

# send_sms(today_reminder)
