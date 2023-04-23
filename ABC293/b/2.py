n = int(input())
a = list(map(int,input().split()))
called = [1] * n
for i in range(n):
    if called[i] == 1:
        called[a[i]-1] = 0
print(sum(called))
ans = []
for i in range(len(called)):
    if called[i] == 1:
        ans.append(i+1)
print(*ans)