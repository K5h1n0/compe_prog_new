n = int(input())
p = list(map(int,input().split()))
cnt = 0
for i in range(1,n+1):
    if i != p[i-1]:
        cnt += 1
if 3 <= cnt:
    print("NO")
else:
    print("YES")