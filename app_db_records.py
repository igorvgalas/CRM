'''This is the app created by Ihor Halas for BNproject CRM.
Retrieve data from Google sheets file for certain date,
modify it and add needed data to database in table Orders and Clients
'''
from datetime import timedelta, date
from data.configdata import spreadsheet_url, sheet_name, database_name
from data.read_order_file import ReadOrderFile
from data.format import Format
from data.db_connector import Connect, Record

curent_date = str(date.today() - timedelta(1))
order_file = ReadOrderFile(spreadsheet_url, sheet_name)
order_file.extract_data(curent_date)
order_list = order_file.to_array().tolist()
sms_list = Format(order_list)
client_list = sms_list.format_phone_number()

conn = Connect(database_name).get_connection()

recorder = Record(conn, client_list)
recorder.record_clients()
recorder.record_orders()

print(f'{curent_date} Done')
