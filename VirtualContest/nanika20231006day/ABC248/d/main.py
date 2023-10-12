from collections import defaultdict
import bisect
n = int(input())
a = list(map(int,input().split()))
d = defaultdict(list)
for i,v in enumerate(a):
    d[v].append(i)
for i in d:
    d[i].sort()
q = int(input())
ans = []
for i in range(q):
    l,r,x = map(int,input().split())
    left_val = bisect.bisect_left(d[x],l-1)
    right_val = bisect.bisect_left(d[x],r)
    ans.append(right_val-left_val)
print(*ans,sep="\n")