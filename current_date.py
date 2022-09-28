'''Module help get date to make a execution app.py'''
from datetime import timedelta
import pandas as pd


def pick_up_date(days):
    '''Function get today date adding a different numbers of days and return 
    a new date for wich we whant execute app.py '''
    curr_date = pd.to_datetime('today').date() + timedelta(days=days)
    return curr_date
