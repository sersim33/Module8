
from datetime import datetime

def get_days_from_today(date):
    
    year, month, day = map(int, date.split('-'))
    
    current_date = datetime.now().date()
    
    specified_date = datetime(year, month, day).date()
    
    difference = current_date - specified_date
    
    return difference.days
    

date = "2019-10-09"
print(get_days_from_today(date))


    

