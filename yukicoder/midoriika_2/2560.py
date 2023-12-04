t = int(input())
ans = []
for _ in range(t):
    n,x = map(int,input().split())
    nowlist = []
    if n*(n+1)//2 <= x:
        for i in range(1,n+1):
            if i == n:
                nowlist.append(x)
            else:
                x -= i
                nowlist.append(i)
    else:
        nowlist.append(-1)
    ans.append(nowlist)
for i in ans:
    print(*i)