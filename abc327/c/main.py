l = []
flg = True
for i in range(9):
    now = list(map(int,input().split()))
    flg &= len(set(now)) == 9
    l.append(now)

for j in range(9):
    nowset = set()
    for i in range(9):
        nowset.add(l[i][j])
    flg &= len(nowset) == 9

for i in range(0,6+1,3):
    for j in range(0,6+1,3):
        
        nowset = set()
        for k in range(3):
            for m in range(3):
                nowset.add(l[i+k][j+m])
        flg &= len(nowset) == 9

if flg:
    print("Yes")
else:
    print("No")