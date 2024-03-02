n = int(input())
ans = []
for i in range(n):
    l = list(map(int,input().split()))
    now = []
    for j in range(1,n+1):
        if l[j-1] == 1:
            now.append(j)
    ans.append(now)
for i in ans:
    print(*i)