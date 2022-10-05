'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''
import warnings
import pandas as pd

if __name__ == "__main__":
    from sms.config import spreadsheet_url, sheet_name


class ReadFile:
    '''Class of ready to read files'''

    def __init__(self, file_url, sheets_name):
        self.file_url = file_url
        self.sheets_name = sheets_name

    def read_orders_file(self):
        '''Read Google Sheeds files and create DateTime column'''
        warnings.simplefilter(action='ignore', category=UserWarning)
        data_frame = pd.read_excel(self.file_url, self.sheets_name)
        data_frame['DateTime'] = data_frame['Date'].astype(
            str) + " " + data_frame['Time'].astype(str)
        return data_frame


if __name__ == "__main__":
    dataframe = ReadFile(spreadsheet_url, sheet_name)
    df = dataframe.read_orders_file()
    print('Data frame was read successfully', df.head())
