l = list(map(int,input().split()))
now = l[0]
if 100 <= now <= 675 and now % 25 == 0:
    pass
else:
    print("No")
    exit()
for i in range(1,8):
    if now > l[i]:
        print("No")
        exit()
    now = l[i]
    if 100 <= now <= 675 and now % 25 == 0:
        continue
    else:
        print("No")
        exit()
print("Yes")