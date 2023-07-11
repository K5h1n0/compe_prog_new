import itertools

s,k = input().split()
s = list(s)
k = int(k)
l = []
for i in itertools.permutations(s,len(s)):
    tmp = ""
    for j in i:
        tmp += j
    l.append(tmp)
l = list(set(l))
l.sort()
print(*l[k-1],sep="")