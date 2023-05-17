n = int(input())
a = list(map(int,input().split()))
rank = [400,800,1200,1600,2000,2400,2800,3200]
l = [0]*8
pref = 0
for i in a:
    flg = 1
    for j in range(len(rank)):
        if i < rank[j]:
            l[j] = 1
            flg = 0
            break
    if flg:
        pref += 1
if sum(l) != 0:
    print(sum(l),sum(l)+pref)
else:
    print(1,pref)