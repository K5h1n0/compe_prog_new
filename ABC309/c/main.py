from collections import defaultdict

n,k = map(int,input().split())
l = []
date = [0]
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
    date.append(a+1)
date.sort()
d = defaultdict(int)
for i,v in enumerate(date):
    d[v] = i
# print(d)
# print(date)
med = [0] * len(date)
for i in l:
    # print(i)
    med[0] += i[1]
    med[d[i[0]+1]] -= i[1]
for i in range(1,len(med)):
    med[i] += med[i-1]
for i in range(len(med)):
    if med[i] <= k:
        if date[i] == 0:
            print(1)
        else:
            print(date[i])
        exit()