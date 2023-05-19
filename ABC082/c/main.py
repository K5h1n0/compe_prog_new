from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)
for i in a:
    d[i] += 1
d_sorted = sorted(d.items())
ans = 0
for i,v in d_sorted:
    if i < v:
        ans += v-i
    elif v < i:
        ans += v
print(ans)