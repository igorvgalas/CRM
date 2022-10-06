'''
This module created by Ihor Halas for BNproject.

Classes:


Functions:


Variable:

'''
import pandas


class ReadOrderFile():
    '''Class of ready to read files'''

    def __init__(self, spreadsheet_url, sheet_name):
        self.spreadsheet_url = spreadsheet_url
        self.sheet_name = sheet_name

    def extract_data(self, date):
        '''Read Google Sheeds files and create DateTime column'''
        self.data_frame = pandas.read_excel(
            self.spreadsheet_url, self.sheet_name)
        self.__filterByDate(date)
        self.__modifyData()

    def toList(self):
        '''Put the data from dataframe to list '''
        self.data_frame = self.data_frame[[
            'Client', 'Phone_number', 'DateTime', 'Service', 'Sum', 'Payment']]
        order_list = self.data_frame.values
        return order_list

    def __filterByDate(self, date):
        self.data_frame = self.data_frame[(self.data_frame['Date'] == date) & (
            self.data_frame['Phone_number'].notna())]

    def __modifyData(self):
        self.data_frame['DateTime'] = self.data_frame['Date'].astype(
            str) + " " + self.data_frame['Time'].astype(str)
