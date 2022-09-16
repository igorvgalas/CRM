'''
This module created by Ihor Halas for BNproject.

Classes:
  OrderDataPrepare
Functions:
   pick_data_by_date
Variable:
   extract_data_to_list 
'''


class OrderDataPreparer:
    '''...'''

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def pick_data_by_date(self, date):
        '''pick up the data by the current date'''
        self.data_frame = self.data_frame[(self.data_frame['Date'] == date) & (
            self.data_frame['Phone_number'].notna())]

    def extract_data_to_list(self):
        '''Put the data from dataframe to list '''
        self.data_frame = self.data_frame[['DateTime',
                                           'Client', 'Phone_number', 'Servise']]
        self.data_frame = self.data_frame.values
