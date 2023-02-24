'''This is the app created by Ihor Halas for BNproject CRM.
Retrieve data from Google sheets file for certain date,
modify it and add needed data to database in table Orders and Clients
'''
import datetime
from configdata import spreadsheet_url, sheet_name, database_name
from data.read_order_file import ReadOrderFile
from data.format import Format
from data.db_connector import Connect, Record
import datetime

#curent_date = str(date.today() - timedelta(1))
start = datetime.datetime.strptime("2023-02-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2023-02-19", "%Y-%m-%d")
date_generated = [(start + datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(0, (end-start).days+1)]

conn = Connect(database_name).get_connection()
for curent_date in date_generated:
    order_file = ReadOrderFile(spreadsheet_url, sheet_name[1])
    order_file.extract_data(curent_date)
    order_list = order_file.to_array().tolist()
    sms_list = Format(order_list)
    client_list = sms_list.format_phone_number()
    recorder = Record(conn, client_list)
    recorder.record_clients()
    recorder.record_orders()

print(f'For {sheet_name[1]} done. Congrats.')


