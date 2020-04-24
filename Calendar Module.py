import calendar
a,b,c=map(int,input().split())
d=list(calendar.day_name)[calendar.weekday(c,a,b)].upper()
print(d)
