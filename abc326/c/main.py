n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
maximum = 0
right = 0
for left in range(n):
    while right < n and a[right]-a[left] < m:
        right += 1
    if left >= right:
        right = left
        continue
    maximum = max(maximum,right-left)
    if left == n:
        break
print(maximum)