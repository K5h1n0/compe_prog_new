x,y,n = map(int,input().split())
ans = 10**10
for i in range(101):
    for j in range(101):
        if i + j*3 == n:
            ans = min(ans,x*i+y*j)
print(ans)