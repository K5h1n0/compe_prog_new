n = int(input())
l = sorted(list(map(int,input().split())))
ans = 0
for i in range(n,len(l)-n):
    ans += l[i]
print(ans/(len(l)-n-n))