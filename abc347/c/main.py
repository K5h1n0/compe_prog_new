import bisect

n,a,b = map(int,input().split())
d = list(map(int,input().split()))
week = a+b
l = []
for i in range(len(d)):
    l.append(d[i]%week)
l.sort()
l2 = l[:]
for i in range(len(l2)):
    l.append(l2[i]+week)
flg = False
#print(l)
for i in range(len(l)):
    right = bisect.bisect_left(l,l[i]+a)
    flg |= right - i >= n
print("Yes" if flg else "No")