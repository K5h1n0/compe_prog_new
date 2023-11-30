l = int(input())
n = int(input())
a = sorted(list(map(int,input().split())))
ans = 0
for i in a:
    if 0 <= l - i:
        l -= i
        ans += 1
    else:
        print(ans)
        exit()
print(ans)