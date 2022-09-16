'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''
import warnings
import pandas as pd


class ReadFile():
    '''...'''

    def __init__(self):
        pass

    def read_orders_file(self, filename, sheet_name):
        '''Read xlsx file and create DateTime column'''
        warnings.simplefilter(action='ignore', category=UserWarning)
        data_frame = pd.read_excel(filename, sheet_name)
        data_frame['DateTime'] = data_frame['Date'].astype(
            str) + " " + data_frame['Time'].astype(str)
        return data_frame
