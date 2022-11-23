'''
This is the app created by Ihor Halas for BNproject CRM.
Retrieve data from Google sheets file for certain date,
modify it.
After that create and send remainding message to the client.
'''
from datetime import timedelta, date
from data.configdata import spreadsheet_url, sheet_name
from data.read_order_file import ReadOrderFile
from data.format import Format
from sms.sms_module import create_sms, send_sms


order_file = ReadOrderFile(spreadsheet_url, sheet_name)
order_file.extract_data(str(date.today() + timedelta(1)))
order_list = order_file.to_array().tolist()

sms_list = Format(order_list)
sms_list.format_phone_number()
formated_sms_list = sms_list.format_date_time()
print(len(formated_sms_list))
today_reminder = create_sms(formated_sms_list)
print(len(today_reminder.keys()))
# send_sms(today_reminder)
