n,q = map(int,input().split())
s = list(input())
ans = []
nowhead = 0
for i in range(q):
    t,x = map(int,input().split())
    if t == 1:
        nowhead = (nowhead - x)%n
    elif t == 2:
        ans.append(s[(nowhead+x)%n-1])
print(*ans,sep="\n")