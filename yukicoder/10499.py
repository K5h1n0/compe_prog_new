t = int(input())
ans = []
for i in range(t):
    v,x,fo,fi,q,r = map(int,input().split())
    now = x + (fi - fo) * r
    if now <= 0:
        ans.append("Zero")
    elif v < now:
        ans.append("Overflow")
    else:
        now -= (q - r) * fo
        if now <= 0:
            ans.append("Zero")
        else:
            if x == now:
                ans.append("Safe")
            elif now < x:
                ans.append("Zero")
            else:
                ans.append("Overflow")
print(*ans,sep="\n")