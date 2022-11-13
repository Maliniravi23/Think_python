from datetime import datetime

def print_current_day_of_week():

    print(datetime.today().strftime('%A'))

print_current_day_of_week()
