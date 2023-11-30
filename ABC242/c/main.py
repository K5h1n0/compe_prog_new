n = int(input())
now = 9
for i in range(1,n):
    now = ((now-2)*3 + (i)*2)%998244353
print(now)