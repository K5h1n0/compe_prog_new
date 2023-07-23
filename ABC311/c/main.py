from collections import defaultdict,deque

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(list)
q = deque()
for i in range(n):
    d[i+1].append(a[i])
ans = []
for i in range(1,n+1):
    l = [0]*(n+1)
    q.append(i)
    l[i] = 1
    while q:
        now = q.popleft()
        for next in d[now]:
            if l[next] == 0:
                l[next] += 1
                q.append(next)
            elif l[next] == 1:
                l[next] += 1
                q.append(next)
                ans.append(next)
    if len(ans) != 0:
        print(len(ans))
        print(*ans)
        exit()
