import datetime

x = datetime.datetime.now()
print(x)

m = x.strftime('%Y')
print(m)
print(x.strftime('%H'))
print(x.strftime('%I'))



# creating date objects

print(datetime.datetime(2022,2,22))