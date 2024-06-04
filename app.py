'''
This is the app created by Ihor Halas for BN studio CRM.
Retrieve data from Google sheets file for certain date,
modify it.
After that create and send reminding message to the client,
modify it and add needed data to database in table Orders and Clients
'''
from configdata import spreadsheet_url, sheet_name, database_name
from data.read_order_file import ReadOrderFile
from data.Format import Format
from sms.sms_module import create_sms, send_sms
from data.db_connector import Connect, Record
from datetime import date, timedelta

today = date.today()
next_day = str(today + timedelta(1))
curent_date = str(today)
curent_month = today.month

order_file = ReadOrderFile(spreadsheet_url, sheet_name[curent_month-1])
order_file.extract_data(next_day)
order_list = order_file.to_array().tolist()

sms_list = Format(order_list)
sms_list.format_phone_number()
formated_sms_list = sms_list.format_date_time()
today_reminder = create_sms(formated_sms_list)
print(today_reminder, next_day)
send_sms(today_reminder)

conn = Connect(database_name).get_connection()
order_file.extract_data(curent_date)
order_list_done = order_file.to_array().tolist()
adding_list = Format(order_list_done)
client_list_done = adding_list.format_phone_number()
recorder = Record(conn, client_list_done)
recorder.record_clients()
recorder.record_orders()


with open("log_file.txt", "a+", encoding="utf-8") as file:
    file.seek(0)
    data = file.read(100)
    if len(data) > 0:
        file.write("\n")
    file.write(
        f'смс нагадування за {next_day} відправлено і запис в БД за {curent_date} проведено успішно')
