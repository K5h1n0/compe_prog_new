n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(len(b)):
    ans += a[b[i]-1]
print(ans)