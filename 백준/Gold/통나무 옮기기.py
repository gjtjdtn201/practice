import datetime

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')
nowDDate = now.strftime('%Y%m%d')
print(nowDate)
print(nowDDate)