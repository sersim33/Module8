from calendar import monthrange
import calendar
from datetime import datetime, timedelta


def days_in_month(month, year):
    # Convert month and year to integers
    month = int(month)
    year = int(year)
    # Use monthrange function to get the number of days in the specified month
    num_days = monthrange(year, month)[1]
    return num_days



print(days_in_month("02", "2023"))