# 解説AC

n,q = map(int,input().split())
l = list(range(n))
p = list(range(n))
for _ in range(q):
    x = int(input())
    x -= 1
    i = p[x]
    j = i + 1
    if j == n:
        j = i - 1
    y = l[j]
    l[i],l[j] = l[j],l[i]
    p[x],p[y] = p[y],p[x]
for i in l:
    print(i+1,end=" ")