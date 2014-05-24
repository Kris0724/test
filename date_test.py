import datetime

def datetime_toString(dt):
    return dt.strftime("%Y%m%d")

for i in range(60 +1 ):
    ii = i*-1
    print datetime_toString( datetime.date.today() + datetime.timedelta(days=ii) )
