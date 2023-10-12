def solver(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i == 0:
            cnt += 1
    if cnt == 8 and n%2 == 1: #奇数かどうかをここで判断できるんだ
        return True
    else:
        return False

N = int(input())
ans = 0
for i in range(1,N+1):
    if solver(i):
        ans += 1
print(ans)