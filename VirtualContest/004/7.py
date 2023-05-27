def f(recycle):
    global m,n,N,ans
    new = recycle//m * n
    ans += new
    if new == 0:
        return
    N = new
    amari = recycle - new
    N += amari
    f(N)

m,n,N = map(int,input().split())
ans = 0
ans += N
f(N)
print(ans)