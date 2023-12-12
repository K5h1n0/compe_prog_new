from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    s = "".join(sorted(list(input())))
    d[s] += 1
ans = 0
for i in d.values():
    ans += (i * (i-1))//2
print(ans)