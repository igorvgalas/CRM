'''This is the app created by Ihor Halas for BN studio CRM.
Retrieve data from Google sheets file for certain date,
modify it.
After that create and send reminding message to the client,
modify it and add needed data to database in table Orders and Clients
'''
from datetime import datetime, timedelta
from configdata import spreadsheet_url, sheet_name, database_name
from data.read_order_file import ReadOrderFile
from data.Format import Format
from data.db_connector import Connect, Record


def get_past_week_dates(start_date=None):
    """ Get the list of dates for the past week """
    if start_date is not None:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    else:
        start_date = datetime.now()
    past_week_dates = [start_date - timedelta(days=i) for i in range(7)]
    return past_week_dates


# Get the list of dates for the past week
past_week_dates = get_past_week_dates("2024-06-03")
conn = Connect(database_name).get_connection()

for curr_date in past_week_dates:
    # Convert the current date to string
    curent_date = str(curr_date)
    curent_month = curr_date.month

    order_file = ReadOrderFile(spreadsheet_url, sheet_name[curent_month-1])
    order_file.extract_data(curent_date)
    order_list_done = order_file.to_array().tolist()
    adding_list = Format(order_list_done)
    client_list_done = adding_list.format_phone_number()
    recorder = Record(conn, client_list_done)
   # print(f'Запис в БД за {client_list_done} проведено успішно')
    recorder.record_clients()
    recorder.record_orders()

    with open("log_file.txt", "a+", encoding="utf-8") as file:
        file.seek(0)
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")
        file.write(f'Запис в БД за {curent_date} проведено успішно')
