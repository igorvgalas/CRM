'''
This module created by Ihor Halas for BNproject.

Classes:
  OrderDataPrepare
Functions:
   pick_data_by_date
Variable:
   extract_data_to_list 
'''
if __name__ == "__main__":
    from data.configdata import spreadsheet_url, sheet_name
    from data.ReadFile import ReadFile


class OrderDataPreparer:
    '''Class of dataframes'''

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def pick_data_by_date(self, date):
        '''Pick up the data by the current date'''
        self.data_frame = self.data_frame[(self.data_frame['Date'] == date) & (
            self.data_frame['Phone_number'].notna())]

    def extract_data_to_list(self):
        '''Put the data from dataframe to list '''
        self.data_frame = self.data_frame[[
            'Client', 'Phone_number', 'DateTime', 'Servise', 'Sum', 'Payment']]
        order_list = self.data_frame.values
        return order_list


if __name__ == "__main__":
    dataframe = ReadFile(spreadsheet_url, sheet_name)
    df = dataframe.read_orders_file()
    dframe = OrderDataPreparer(df)
    dframe.pick_data_by_date(date='2022-10-01')
    mlist = dframe.extract_data_to_list()
    print(mlist)
