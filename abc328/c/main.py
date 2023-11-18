n,q = map(int,input().split())
s = input()
accum = [0]*(n+1)
tmp = ""
for i in range(n):
    if s[i] == tmp:
        accum[i] += 1
    tmp = s[i]
for i in range(n):
    accum[i+1] += accum[i]
ans = []
for i in range(q):
    l,r = map(int,input().split())
    if r <= l:
        ans.append(0)
        continue
    ans.append(accum[r-1] - accum[l-1])
print(*ans,sep="\n")