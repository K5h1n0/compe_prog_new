from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d1 = defaultdict(int)
d2 = defaultdict(int)
for i in range(n):
    d1[i+1] = a[i]
    d2[a[i]] = i+1

ans = []
for i in range(1,n+1):
    if i != d1[i]:
        ans.append([i,d2[i]])
        tmp = d1[i]

        w = d1[d2[i]]
        d1[d2[i]] = d1[i]
        d1[i] = w
        
        w2 = d2[i]
        d2[tmp] = w2
        d2[i] = i
print(len(ans))
for i in ans:
    print(*i)