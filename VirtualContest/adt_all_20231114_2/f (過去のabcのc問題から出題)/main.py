n = int(input())
bi = bin(n)[2:][::-1]
numlist = []
for i in range(len(bi)):
    if bi[i] == "1":
        numlist.append(2**i)

ans = []
for i in range(2**len(numlist)):
    now = 0
    for j in range(len(numlist)):
        if ((i >> j)&1):
            now += numlist[j]
    ans.append(now)
ans.sort()
print(*ans,sep="\n")