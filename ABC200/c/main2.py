from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)
for i in a:
    d[i%200] += 1
ans = 0
for i in d.values():
    ans += (i * (i-1))//2
print(ans)