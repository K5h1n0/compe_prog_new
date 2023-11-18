n = int(input())
d = list(map(int,input().split()))
ans = 0
for i in range(1,n+1):
    for j in range(1,d[i-1]+1):
        if len(set(list(str(i)+str(j)))) == 1:
            ans += 1
print(ans)