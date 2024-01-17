n = int(input())
t = list(map(int,input().split()))
m = int(input())
ans = []
total = sum(t)
for i in range(m):
    p,x = map(int,input().split())
    ans.append(total-t[p-1]+x)
print(*ans,sep="\n")