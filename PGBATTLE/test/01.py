n,m = map(int,input().split())
if n >= m:
    print(0)
    exit()
ans = (m-n+9)//10
print(ans)