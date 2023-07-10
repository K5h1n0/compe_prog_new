from collections import deque,defaultdict

n1,n2,m = map(int,input().split())
l = []
d1 = defaultdict(list)
d2 = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    if max(a,b) <= n1:
        d1[a].append(b)
        d1[b].append(a)
    else:
        d2[a].append(b)
        d2[b].append(a)
# print(d1)
# print(d2)
n1_list = [0] * (n1+1)
q1 = deque()
n1_list[1] = -1
q1.append([1,0])
while q1:
    tmp,nowcnt = q1.popleft()
    nowcnt += 1
    for i in d1[tmp]:
        if n1_list[i] == 0:
            n1_list[i] = nowcnt
            q1.append([i,nowcnt])

n2_list = [0] * (n1+n2+1)
q2 = deque()
n2_list[n1+n2] = -1
q2.append([n1+n2,0])
while q2:
    tmp,nowcnt = q2.popleft()
    nowcnt += 1
    for i in d2[tmp]:
        if n2_list[i] == 0:
            n2_list[i] = nowcnt
            q2.append([i,nowcnt])
# print(n1_list)
# print(n2_list)
print(max(n1_list)+max(n2_list)+1)