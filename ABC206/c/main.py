from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)
for i in range(len(a)):
    d[a[i]] += 1
total = len(a)
ans = 0
for i in d.values():
    ans += i * (total-i)
print(ans//2)