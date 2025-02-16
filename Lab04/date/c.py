import datetime
current_datetime = datetime.datetime.now()
changed = current_datetime.replace(microsecond=0)
print(f"Datetime without microseconds: {changed}")