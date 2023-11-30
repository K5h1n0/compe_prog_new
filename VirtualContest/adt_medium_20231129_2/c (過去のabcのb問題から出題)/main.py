a,b,k = map(int,input().split())
ans = 0
for i in range(1,100):
    if b <= a:
        print(ans)
        exit()
    ans += 1
    a *= k