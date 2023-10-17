from collections import defaultdict

q = int(input())
l = []
d = defaultdict(int)
for i in range(q):
    type, *arg = map(int,input().split())
    if type == 1:
        d[arg[0]] += 1
    elif type == 2:
        d[arg[0]] = max(0,d[arg[0]]-arg[1])
    elif type == 3:
        print(d)