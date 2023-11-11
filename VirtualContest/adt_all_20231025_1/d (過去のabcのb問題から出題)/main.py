n = int(input())
l = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    l[a] += 1
    l[b] += 1
if max(l) == n-1:
    print("Yes")
else:
    print("No")