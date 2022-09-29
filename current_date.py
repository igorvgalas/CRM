'''Module help get date to make a execution app.py'''
from datetime import timedelta
import pandas as pd


def pick_up_date(days):
    '''Function get today date adding a different numbers of days and return 
    a new date for wich we whant execute app.py '''
    curr_date = pd.to_datetime('today').date() + timedelta(days=days)
    return curr_date


if __name__ == "__main__":
    DAY = 1
    my_date = pick_up_date(DAY)
    print(my_date)
# shows next date from today
