n,q = map(int,input().split())
s = input()
ans = []
start = 0
for i in range(q):
    t,x = map(int,input().split())
    if t == 1:
        start = (start - x)%n
    elif t == 2:
        ans.append(s[(start + x)%n-1])
print(*ans,sep="\n")