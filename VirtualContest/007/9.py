n = int(input())
h = list(map(int,input().split()))
h2 = list(map(lambda x: x-1,h))
ans = "Yes"
now = h[-1]
for i in range(n-1,-1,-1):
    if h[i] <= now:
        now = h[i]
        pass
    elif h[i]-1 <= now:
        now = h[i]-1
    else:
        ans = "No"
print(ans)