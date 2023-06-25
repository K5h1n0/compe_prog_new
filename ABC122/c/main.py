n,q = map(int,input().split())
s = list(input())
l = [0]*len(s)
for i in range(1,len(l)):
    if s[i-1] == "A" and s[i] == "C":
        l[i-1] = 2
        l[i] = 1
print(l)
for i in range(1,len(l)):
    l[i] += l[i-1]
ans = []
for i in range(q):
    left,right = map(int,input().split())
    ln = l[left]
    rn = l[right-1]
    if ln%3 != 0:
        ln = l[left+1]
    if rn%3 != 0:
        rn = l[right-1]
    ans.append(rn-ln)
print(l)
print(*ans,sep="\n")