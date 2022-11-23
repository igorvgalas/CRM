from data.configdata import database_name
from data.db_connector import Connect, TakeRecords
from sms.sms_module import create_sms_to_all, send_sms


conn = Connect(database_name).get_connection()
all_clients = TakeRecords(conn)
all_clients_list = all_clients.clients_records()
print(len(all_clients_list))
sms_to_all = create_sms_to_all(all_clients_list)
print(len(sms_to_all.keys()))
# print(sms_to_all)
# send_sms(sms_to_all)
