from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)
for i in range(len(a)):
    d[a[i]] += 1
len_a = len(a)
ans = ((1+len_a)*len_a)//2
print(ans)
for i in d:
    print(d[i])
    ans -= d[i]
print(ans)