k,x = map(int,input().split())
ans = []
for i in range(x-k+1,x+k):
    ans.append(i)
print(*ans)