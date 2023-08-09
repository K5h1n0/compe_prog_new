from collections import defaultdict,deque

n,m = map(int,input().split())
d = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    d[b].append(a)
l = [0]*(n+1)
for i in range(1,n+1):
    q = deque()
    visited = [0] * (n+1)
    q.append(i)
    # print("スタート",i)
    while q:
        now = q.popleft()
        if now not in d:
            # print("Hello")
            # print("今は",now)
            l[now] += 1
            break
        else:
            for next in d[now]:
                if visited[next] == 0:
                    q.append(next)
                    # print(next,"をpush")
ans = -1
for i in range(len(l)):
    if l[i] == 0:
        continue
    elif l[i] != 0 and ans == -1:
        ans = i
    elif l[i] != 0 and ans != -1:
        print(-1)
        exit()
print(ans)