n = int(input())
a = list(map(int,input().split()))

ruiseki_max1 = [0] * len(a)
ruiseki_max2 = [0] * len(a)
maximum1 = 0
maximum2 = 0
for i in range(len(a)):
    maximum1 = max(maximum1,a[i])
    maximum2 = max(maximum2,a[-i-1])
    ruiseki_max1[i] = maximum1
    ruiseki_max2[-i-1] = maximum2

d = int(input())
ans = []
for i in range(d):
    l,r = map(int,input().split())
    tmp = max(ruiseki_max1[l-2],ruiseki_max2[r])
    ans.append(tmp)
print(*ans,sep="\n")