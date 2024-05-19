from collections import deque

n = int(input())
l = []
for i in range(1,n+1):
    a,c = map(int,input().split())
    l.append([c,a,i])
l.sort(reverse=True)
ans = []
d = deque()
d.append(l[0])
for i in range(1,n):
    flg = 1
    pre = d.pop()
    now = l[i]
    while pre[1] < now[1]:
        if len(d) == 0:
            flg = 0
            break
        pre = d.pop()
    if flg:
        d.append(pre)
    d.append(now)
ans = []
for i in d:
    ans.append(i[2])
ans.sort()
print(len(ans))
print(*ans)