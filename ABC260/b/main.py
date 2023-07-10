n,x,y,z = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
la = []
lb = []
lc = []
for i in range(n):
    la.append((a[i],i))
    lb.append((b[i],i))
    lc.append((a[i] + b[i],i))
bool_list = [0]*n
ans = []
la.sort(reverse=True)
lb.sort(reverse=True)
lc.sort(reverse=True)
cnt = 0
i = 0
print(la)
print(lb)
print(lc)
while cnt < x:
    if bool_list[la[i][1]] == 0:
        ans.append(la[i][1]+1)
        bool_list[la[i][1]] = 1
        cnt += 1
    i += 1
cnt = 0
i = 0
while cnt < y:
    if bool_list[lb[i][1]] == 0:
        ans.append(lb[i][1]+1)
        bool_list[lb[i][1]] = 1
        cnt += 1
    i += 1
cnt = 0
i = 0
while cnt < z:
    if bool_list[lc[i][1]] == 0:
        ans.append(lc[i][1]+1)
        bool_list[lc[i][1]] = 1
        cnt += 1
    i += 1
ans.sort()
print(*ans,sep="\n")