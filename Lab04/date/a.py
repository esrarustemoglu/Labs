import datetime
current_date = datetime.datetime.today()
new_date = current_date - datetime.timedelta(days=5)
print(new_date.strftime('%Y-%m-%d'))