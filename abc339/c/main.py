n = int(input())
a = list(map(int,input().split()))
now = 0
mustadd = 0
for i in range(n):
    now += a[i]
    mustadd = min(mustadd,now)
mustadd = abs(mustadd)
now = 0
for i in range(n):
    now += a[i]
now += mustadd
print(now)