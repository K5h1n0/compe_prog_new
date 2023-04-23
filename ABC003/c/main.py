n,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
now = float(0)
for i in range(n-k,n):
    now = (now + l[i])/2
print(now)