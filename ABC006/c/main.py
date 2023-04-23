#??
n,m = map(int,input().split())
for i in range(n):
    for j in range(n):
        total = i * 3 + j * 4
        remain = m - total
        if remain < 0 or n <= i + j:
            break
        if remain%2 == 0 and 0 <= remain and i + j + remain//2 == n:
            print(remain//2,i,j)
            exit()
print(-1,-1,-1)