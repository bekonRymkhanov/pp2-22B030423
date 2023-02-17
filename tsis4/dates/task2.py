from datetime import datetime
x=datetime.now()
print(x.strftime("%Y-%m"),x.day+1,sep="-")
print(x.strftime("%Y-%m-%d"))
print(x.strftime("%Y-%m"),x.day-1,sep="-")
