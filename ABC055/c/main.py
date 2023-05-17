n,m = map(int,input().split())
if m//2 < n:
    print(m//2)
else:
    m -= n*2
    print(n+m//4)