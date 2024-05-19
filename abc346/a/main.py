n = int(input())
l = list(map(int,input().split()))
ans = []
for i in range(1,n):
    ans.append(l[i-1]*l[i])
print(*ans)