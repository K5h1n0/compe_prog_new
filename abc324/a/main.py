n = int(input())
l = list(map(int,input().split()))
a = l[0]
flg = True
for i in range(n):
    flg &= a == l[i]
if flg:
    print("Yes")
else:
    print("No")