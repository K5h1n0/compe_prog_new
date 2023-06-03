from collections import defaultdict,deque

n,d = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
dic = defaultdict(list)
for i in range(n-1):
    for j in range(i+1,n):
        if ((l[i][0] - l[j][0])**2 + (l[i][1] - l[j][1])**2)**0.5 <= d:
            dic[i].append(j)
            dic[j].append(i)
q = deque()
infect = [0]*n
q.append(0)
infect[0] = 1
while q:
    now = q.popleft()
    for next in dic[now]:
        if infect[next] == 0:
            q.append(next)
            infect[next] = 1
for i in infect:
    if i == 0:
        print("No")
    else:
        print("Yes")