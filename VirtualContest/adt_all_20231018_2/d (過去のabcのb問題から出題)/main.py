n = int(input())
p = list(map(int,input().split()))
next = p[-1]-1
ans = 1
if next == 0:
    print(ans)
    exit()
for i in range(51):
    next = p[next-1]-1
    ans += 1
    if next == 0:
        print(ans)
        exit()