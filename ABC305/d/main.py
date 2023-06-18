from collections import defaultdict
import bisect

n = int(input())
a = list(map(int,input().split()))
q = int(input())
all = a[:]
l =[]
for i in range(q):
    left,right = map(int,input().split())
    all.append(left)
    all.append(right)
    l.append([left,right])
all = sorted(list(set(all)))
d = defaultdict(int)
for i,v in enumerate(all):
    d[v] = i
allflg = [9]*len(all)
for i in range(len(a)):
    if i % 2 == 0:
        allflg[bisect.bisect_right(all,a[i])-1] = 0
    else:
        allflg[bisect.bisect_right(all,a[i])-1] = 1
# print(a)
# print(all)
# print(allflg)
l2 = []
tmp = 0
for i in range(len(all)):
    if allflg[i] == 0:
        flg = 0
        l2.append(all[i]-tmp)
        tmp = all[i]        
    elif allflg[i] == 1:
        tmp = all[i]
        l2.append(0)
        flg = 1
    elif allflg[i] == 9:
        if flg == 0:
            l2.append(0)
        else:
            l2.append(all[i]-tmp)
            tmp = all[i]
tmp = 0
for i in range(len(l2)):
    l2[i] = tmp+l2[i]
    tmp = l2[i]
ans = []
for i in range(len(l)):
    ans.append(l2[d[l[i][1]]] - l2[d[l[i][0]]])
print(*ans,sep="\n")