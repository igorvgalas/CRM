'''
This is the app created by Ihor Halas for BN studio CRM.
Retrieve data from Google sheets file for certain date,
modify it.
After that create and send reminding message to the client,
modify it and add needed data to database in table Orders and Clients
'''
from datetime import date, timedelta
from configdata import spreadsheet_url, sheet_name
from data.read_order_file import ReadOrderFile
from data.Format import Format
from sms.sms_module import create_sms, send_sms

today = date.today()
next_day = today + timedelta(1)
current_month = next_day.month
print(current_month)
order_file = ReadOrderFile(spreadsheet_url, sheet_name[current_month-1])
print(sheet_name[current_month-1])
order_file.extract_data(str(next_day))

order_list = order_file.to_array().tolist()
print(order_list)
sms_list = Format(order_list)
sms_list.format_phone_number()
formated_sms_list = sms_list.format_date_time()
today_reminder = create_sms(formated_sms_list)
# print(today_reminder)
send_sms(today_reminder)

with open("log_file.txt", "a+", encoding="utf-8") as file:
    file.seek(0)
    data = file.read(100)
    if len(data) > 0:
        file.write("\n")
    file.write(f'Відправка смс за {next_day} проведено успішно')
