k,n,f = map(int,input().split())
a = list(map(int,input().split()))
if 0 <= k*n - sum(a):
    print(k*n - sum(a))
else:
    print(-1)