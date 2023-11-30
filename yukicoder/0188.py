import datetime
now = datetime.datetime(2014,12,31,0,0,0)
cnt = 0
for i in range(365):
    now += datetime.timedelta(days=1)
    if int(now.month) == sum(list(map(int,str(now.day)))):
        cnt += 1
print(cnt)