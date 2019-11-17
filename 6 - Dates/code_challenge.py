from datetime import datetime, timedelta
# print today's date
todays_date = datetime.now()
print(f'Today: {todays_date}')
# print yesterday's date
one_day = timedelta(days=1)
print(f'Yesterday: {todays_date - one_day}')
# ask a user to enter a date
# print the date one week from the date entered
one_week = timedelta(weeks=1)
user_input = input('Please input a date (mm/dd/yyyy): ')
user_date = datetime.strptime(user_input, '%m/%d/%Y')
plus_one_week = datetime.strftime(user_date + one_week, '%m/%d/%Y')
print (f'One week from the entered date is {plus_one_week}')