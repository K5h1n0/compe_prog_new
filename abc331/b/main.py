n,s,m,l = map(int,input().split())
ans = []
for i in range(101):
    for j in range(101):
        for k in range(101):
            if n <= i*6 + j*8 + k*12:
                ans.append(s*i+m*j+l*k)
print(min(ans))