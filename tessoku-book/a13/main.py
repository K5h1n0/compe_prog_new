n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
right = 0
now = 0
tmp = 0
for left in range(n):
    while right < n and a[right] - a[left] <= k:
        right += 1
    # print(f"left{left},right{right}")
    if left == right:
        right += 1
        continue
    ans += right-1 - left #これが結構混乱するかも。半開区間で考えて、区間にrightのポイントは含まないので-1。
print(ans)