from collections import defaultdict,deque
import copy

def f(str1,str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] in str2:
            cnt += 1
            str2.remove(str1[i])
    return cnt

n,m = map(int,input().split())
l = []
for i in range(n):
    l.append(list(input()))
d = defaultdict(list)
for i in range(n-1):
    for j in range(i+1,n):
        tmp1 = copy.copy(l[i])
        tmp2 = copy.copy(l[j])
        if f(tmp1,tmp2) == m-1:
            d[i].append(j)
            d[j].append(i)

for i in range(n):
    q = deque()
    bo = [0]*n
    q.append(i)
    bo[i] = 1
    while q:
        tmp = q.popleft()
        for j in d[tmp]:
            if bo[j] == 0:
                q.append(j)
                bo[j] = 1
    if sum(bo) == n:
        print("Yes")
        exit()
print("No")