from collections import defaultdict

n,m = map(int,input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int,input().split()))
menu = defaultdict(int)
for i in range(len(d)):
    menu[d[i]] = p[i+1]
d = set(d)
total = 0
for i in c:
    if i in d:
        total += menu[i]
    else:
        total += p[0]
print(total)