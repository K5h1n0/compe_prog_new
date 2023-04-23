#解説AC
n = int(input())
ans = 0
for i in range(1,1000001):
    tmp = str(i)+str(i)
    if int(tmp) <= n:
        ans += 1
print(ans)