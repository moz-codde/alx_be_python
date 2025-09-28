import datetime as dt
from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    number_of_days = input("Enter the number of days to add to the current date:")
    current_date = datetime.now()
    future_date = datetime.now() + dt.timedelta(days=int(number_of_days))
    print(future_date.strftime("%Y-%m-%d"))
