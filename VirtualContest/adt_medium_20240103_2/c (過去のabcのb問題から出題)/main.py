n = int(input())
l = [0]*n
for _ in range(n-1):
    a,b = map(int,input().split())
    l[a-1] += 1
    l[b-1] += 1
flg = True
for i in range(n):
    flg &= 1 <= l[i]
if flg and max(l) == n-1:
    print("Yes")
else:
    print("No")