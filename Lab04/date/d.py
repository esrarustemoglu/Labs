import datetime
date1 = datetime.datetime(2025, 2, 15, 13, 20, 0)
date2 = datetime.datetime(2024, 12, 31, 23, 59, 0)
dif =( date1- date2).total_seconds()
print(dif)