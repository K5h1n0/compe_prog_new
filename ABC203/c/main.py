from collections import defaultdict

n,k = map(int,input().split())
d = defaultdict(int)
for i in range(n):
    a,b = map(int,input().split())
    d[a] += b
d2 = sorted(d.items())
now = 0
for i,v in d2:
    if now + k - i < 0:
        print(now+k)
        exit()
    else:
        now += i
        k -= i
        k += v
print(now+k)