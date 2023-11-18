n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
flg = True
for i in range(m):
    if b[i] in a:
        a.remove(b[i])
    else:
        flg = False
if flg:
    print("Yes")
else:
    print("No")