import bisect

d = int(input())
l = [i**2 for i in range(1420000)]
ans = []
for i in range(len(l)):
    now = abs(l[i]-d)
    idx = bisect.bisect_left(l,now)
    # print(l[i],d,now,idx,l[idx-1],abs(l[i]+l[idx-1]-d))
    ans.append(abs(l[i]+l[idx-1]-d))
    ans.append(abs(l[i]+l[idx]-d))
print(min(ans))