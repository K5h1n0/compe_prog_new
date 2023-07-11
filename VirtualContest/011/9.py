n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
print(*l,sep="\n")