n,m = map(int,input().split())
l = list(map(int,input().split()))
ans = list(range(0,n+1))
l2 = []
flg = 0
start = 0
end = 0
for i in range(1,n+1):
    if i in l:
        if flg == 0:
            start = i
            flg = 1
        if flg == 1:
            pass
    else:
        if flg == 0:
            l2 += [i]
        else:
            end = i
            l2 += list(range(start,end+1))[::-1]
            flg = 0
if flg == 1:
    end = n
    l2 += list(range(start,end+1))[::-1]
print(*l2)
