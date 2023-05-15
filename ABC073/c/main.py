from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    d[int(input())] += 1

ans = 0
for v in d.values():
    if v % 2 == 1:
        ans += 1
print(ans)