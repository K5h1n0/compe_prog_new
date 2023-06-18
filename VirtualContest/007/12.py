from collections import defaultdict

n = int(input())
l = []
march = {"M","A","R","C","H"}
d = defaultdict(int)
for i in range(n):
    tmp = input()
    if tmp[0] in march:
        d[tmp[0]] += 1
l2 = list(d.values())
if len(l2) < 3:
    print(0)
else:
    ans = 0
    for i in range(len(l2)-2):
        for j in range(i+1,len(l2)-1):
            for k in range(j+1,len(l2)):
                ans += l2[i]*l2[j]*l2[k]
    print(ans)