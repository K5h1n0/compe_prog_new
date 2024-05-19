n = int(input())
l = list(map(int,input().split()))
now = 0
for i in range(n-1):
    now += l[i]
print(-now)