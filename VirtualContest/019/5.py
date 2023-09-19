n,m = map(int,input().split())
l = set(range(1,n+1))
lose = set()
for i in range(m):
    a,b = map(int,input().split())
    lose.add(b)
if len(l-lose) == 1:
    print(*l-lose)
else:
    print(-1)