

from datetime import datetime


def get_days_from_today(date):
   
    date_string = '2020-10-09'
    date = datetime.strptime(date_string, '%Y-%m-%d')
    current_datetime = datetime.now()
    
    difference = current_datetime - date


    return difference

    
print(get_days_from_today("2021-10-09"))