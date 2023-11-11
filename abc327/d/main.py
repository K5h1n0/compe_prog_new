from collections import defaultdict,deque

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = defaultdict(list)
for i in range(m):
    d[a[i]].append(b[i])
    d[b[i]].append(a[i])
zeroonel = [-1]*(n+1)

for i in range(1,n+1):
    if zeroonel[i] != -1:
        continue
    q = deque()
    q.append(i)
    zeroonel[i] = 0
    while q:
        now = q.popleft()
        for next in d[now]:
            if zeroonel[next] != -1:
                if zeroonel[next] == zeroonel[now]:
                    print("No")
                    exit()
                continue
            
            zeroonel[next] = 1- zeroonel[now]
            q.append(next)
print("Yes")