from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 0
d = defaultdict(int)
for i in c:
    d[b[i-1]] += 1
for i in a:
    ans += d[i]
print(ans)