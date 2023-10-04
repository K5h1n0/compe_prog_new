h,w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(input()))
print(*a,sep="\n")
