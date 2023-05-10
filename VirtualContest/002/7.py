n = int(input())
a = list(map(int,input().split()))
b = set(a)
if 0 in b:
    print(0)
    exit()
a.sort(reverse=True)
ans = 1
for i in range(len(a)):
    ans *= a[i]
    if 10**18 < ans:
        ans = -1
        break
print(ans)