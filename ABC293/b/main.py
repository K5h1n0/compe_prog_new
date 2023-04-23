n = int(input())
l = list(map(int,input().split()))
l = [0] + l
already = set()
p = set(range(1,n+1))
lbl = [False] * len(l)
for i in range(1,len(l)):
    if l[i] in p and lbl[i] == False:
        p.remove(l[i])
        lbl[l[i]] = True
print(len(p))
print(*p)