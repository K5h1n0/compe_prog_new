n,q = map(int,input().split())
s = list(input())
accum = [0]*(n+1)
for i in range(1,n+1):
    if s[i-1] == "A" and s[i] == "C":
        accum[i] += 1
for i in range(1,n+1):
    accum[i] += accum[i-1]
ans = []
for i in range(q):
    l,r = map(int,input().split())
    r -= 1
    if l >= r:
        ans.append(0)
        continue
    ans.append(accum[r]-accum[l-1])
print(*ans,sep="\n")