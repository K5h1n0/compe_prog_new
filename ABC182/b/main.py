n = int(input())
a = list(map(int,input().split()))
gcddo = 0
maximum = max(a)
for i in range(2,maximum+1):
    cnt = 0
    for j in range(n):
        if not a[j] % i:
            cnt += 1
    if gcddo < cnt:
        gcddo = cnt
        ans = i
print(ans)