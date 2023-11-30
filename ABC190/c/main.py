n,m = map(int,input().split())
l = []
for _ in range(m):
    l.append(list(map(int,input().split())))
k = int(input())
l2 = []
for _ in range(k):
    l2.append(list(map(int,input().split())))

maximum = 0
for i in range(2**k):
    nowset = set()
    for j in range(k):
        if (i >> j) & 1 == 1:
            nowset.add(l2[j][0])
        else:
            nowset.add(l2[j][1])

    nowcnt = 0    
    for j in range(len(l)):
        flg = l[j][0] in nowset and l[j][1] in nowset
        if flg:
            nowcnt += 1
    maximum = max(maximum,nowcnt)
print(maximum)