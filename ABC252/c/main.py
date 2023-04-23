n = int(input())
l = []
for i in range(n):
    l.append(input())
l2 = []
for i in range(10):
    # 数字
    l3 = [0]*10
    for j in range(n):
        # 上から何番目か
        tmp = l[j]
        for k in range(10):
            if tmp[k] == str(i):
                l3[k]+=1
                break
    if max(l3) == 1:
        maximum = 0
        for k in range(10):
            if l3[k] != 0:
                maximum = k
        l2.append(maximum)
    else:
        for k in range(9,-1,-1):
            if l3[k] == max(l3):
                l2.append((l3[k]-1)*10+k)
                break
print(min(l2))