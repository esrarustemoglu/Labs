import datetime
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(f" Yesterday was: {yesterday.strftime('%d %B %Y')}")
print(f" Today is: {today.strftime('%d %B %Y')}")
print(f" Tomorrow will: {tomorrow.strftime('%d %B %Y')}")