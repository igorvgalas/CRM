'''
This module created by Ihor Halas for BNproject.

Classes:
ReadOrderFile

Functions:
extract_data
to_array
__filter_by_date
__modify_data

'''
import ssl
import pandas
ssl._create_default_https_context = ssl._create_unverified_context


class ReadOrderFile:
    '''Class of ready to read files'''

    def __init__(self, spreadsheet_url, sheet_name):
        self.spreadsheet_url = spreadsheet_url
        self.sheet_name = sheet_name
        self.data_frame = None

    def extract_data(self, date):
        '''Read Google Sheeds files and create DateTime column'''
        self.data_frame = pandas.read_excel(
            self.spreadsheet_url, self.sheet_name)
        self.__filter_by_date(date)
        self.__modify_data()

    def to_array(self):
        '''Put the data from dataframe to list '''
        self.data_frame = self.data_frame[[
            'Client', 'Phone_number', 'DateTime', 'Service', 'Sum', 'Payment']]
        ndarray = self.data_frame.values
        print(ndarray)
        return ndarray

    def __filter_by_date(self, date):
        '''Filtering data_frame by certain date and phone_number that is not na'''

        # Ensure the 'Date' column is in datetime format
        self.data_frame['Date'] = pandas.to_datetime(self.data_frame['Date'])

        # Normalize the time component to midnight
        # or just focus on the date component for comparison
        self.data_frame['Date'] = self.data_frame['Date'].dt.normalize()

        # Convert input date string to datetime,
        # ensuring it matches the format of the DataFrame's 'Date' column
        filter_date = pandas.to_datetime(date).normalize()

        # Now filter the DataFrame
        self.data_frame = self.data_frame[(self.data_frame['Date'] == filter_date) & (
            self.data_frame['Phone_number'].notna())]

    def __modify_data(self):
        '''Makes new column DateTime'''
        self.data_frame['DateTime'] = self.data_frame['Date'].astype(
            str) + " " + self.data_frame['Time'].astype(str)
