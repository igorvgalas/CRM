'''This is the app created by Ihor Halas for BNproject CRM.
Retrieve data from Google sheets file for certain date,
modify it and add needed data to database in table Orders and Clients
'''
import datetime
from configdata import spreadsheet_url, sheet_name, database_name
from data.read_order_file import ReadOrderFile
from data.format import Format
from data.db_connector import Connect, Record
from datetime import date, timedelta


#curent_date = str(date.today() - timedelta(1))
# start = datetime.datetime.strptime("2023-03-20", "%Y-%m-%d")
# end = datetime.datetime.strptime("2023-03-26", "%Y-%m-%d")
start = date.today()-timedelta(6)
end = date.today()
date_generated = [(start + datetime.timedelta(days=x)).strftime("%Y-%m-%d")
                  for x in range(0, (end-start).days+1)]

conn = Connect(database_name).get_connection()
for curent_date in date_generated:
    order_file = ReadOrderFile(spreadsheet_url, sheet_name[3])
    order_file.extract_data(curent_date)
    order_list = order_file.to_array().tolist()
    sms_list = Format(order_list)
    client_list = sms_list.format_phone_number()
    recorder = Record(conn, client_list)
    recorder.record_clients()
    recorder.record_orders()

with open("~/Baeaty_Nails_Data/CRM/log_file.txt", "a+", encoding="utf-8") as file:
    file.seek(0)
    data = file.read(100)
    if len(data)>0:
        file.write("\n")
    file.write(f'{start} - {end} запис в базу даних проведено успішно')

