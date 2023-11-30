n,l = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if l <= a[i]:
        cnt += 1
print(cnt)