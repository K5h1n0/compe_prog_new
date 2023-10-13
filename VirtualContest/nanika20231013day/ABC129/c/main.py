n, m = map(int,input().split())
stairs = [0]*(n+1)
a = set()
for i in range(m):
    a.add(int(input()))
stairs[0] = 1
for i in range(1,n+1):
    if i in a:
        continue
    stairs[i] += stairs[i-1]
    if i == 1:
        continue
    stairs[i] += stairs[i-2]
    stairs[i] %= 10**9+7
print(stairs[-1])