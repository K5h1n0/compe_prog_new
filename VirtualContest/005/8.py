from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
ans = 0
d = defaultdict(int)
for i in range(len(a)):
    d[a[i]] += 1
d = sorted(d.items(),reverse=True)
l = []
for i in d:
    if 2 <= i[1]:
        l.append(i)
if 1 <= len(l) and 4 <= l[0][1]:
    print(l[0][0]**2)
elif 2 <= len(l):
    print(l[0][0]*l[1][0])
else:
    print(0)