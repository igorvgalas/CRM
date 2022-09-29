'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''
import warnings
import pandas as pd

if __name__ == "__main__":
    from config import spreadsheet_url, sheet_name


class ReadFile():
    '''Class of ready to read files'''

    def __init__(self):
        pass

    def read_orders_file(self, filename, sheetname):
        '''Read Google Sheeds files and create DateTime column'''
        warnings.simplefilter(action='ignore', category=UserWarning)
        data_frame = pd.read_excel(filename, sheetname)
        data_frame['DateTime'] = data_frame['Date'].astype(
            str) + " " + data_frame['Time'].astype(str)
        return data_frame


if __name__ == "__main__":
    dataframe = ReadFile()
    df = dataframe.read_orders_file(spreadsheet_url, sheet_name)
    print('Data frame was read successfully', df.head())
