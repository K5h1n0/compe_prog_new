from collections import defaultdict

n,m = map(int,input().split())
a = list(map(int,input().split()))
d = defaultdict(int)
ans = []
nowmaxnum = a[0]
ans.append(a[0])
d[a[0]] += 1
nowmax = 1
for i in range(1,len(a)):
    d[a[i]] += 1
    if nowmax < d[a[i]]:
        nowmax = d[a[i]]
        nowmaxnum = a[i]
    elif d[a[i]] < nowmax:
        pass
    else:
        if a[i] < nowmaxnum:
            nowmax = d[a[i]]
            nowmaxnum = a[i]
        else:
            pass
    ans.append(nowmaxnum)
print(*ans,sep="\n")