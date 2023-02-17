from datetime import datetime
x=datetime(2020,12,23,12,22,23)
y=datetime(2020,2,2,21,3,34)
a=((x.year-y.year)*31471200+(x.month-y.month)*2592000+(x.day-y.day)*86400+(x.hour-y.hour)*3600+(x.minute-y.minute)*60+(x.second-y.second))
print(a)