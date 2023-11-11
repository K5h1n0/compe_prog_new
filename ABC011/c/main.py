#貪欲
#DPのやりかたはちょっと分からない
n = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())
nglist = sorted([ng1,ng2,ng3])
if n in nglist:
    print("NO")
    exit()
for i in range(100):
    if n-3 not in nglist:
        n -= 3
    elif n-2 not in nglist:
        n -= 2
    elif n-1 not in nglist:
        n -= 1
    else:
        print("NO")
        exit()
if n <= 0:
    print("YES")
else:
    print("NO")
