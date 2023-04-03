'''
This is the app created by Ihor Halas for BNproject CRM.
Retrieve data from Google sheets file for certain date,
modify it.
After that create and send reminding message to the client.
'''
from datetime import timedelta, date
from configdata import spreadsheet_url, sheet_name
from data.read_order_file import ReadOrderFile
from data.format import Format
from sms.sms_module import create_sms, send_sms


order_file = ReadOrderFile(spreadsheet_url, sheet_name[2])
curent_date = str(date.today() + timedelta(0))
order_file.extract_data(curent_date)
order_list = order_file.to_array().tolist()

sms_list = Format(order_list)
sms_list.format_phone_number()
formated_sms_list = sms_list.format_date_time()
today_reminder = create_sms(formated_sms_list)
#print(today_reminder)
send_sms(today_reminder)

with open("~/Baeaty_Nails_Data/CRM/log_file.txt", "a+", encoding="utf-8") as file:
    file.seek(0)
    data = file.read(100)
    if len(data)>0:
        file.write("\n")
    file.write(f'{curent_date} смс нагадування відправлено успішно')
