n,t = input().split()
n = int(n)
tlen = len(t)
lackone = set()
for i in range(len(t)):
    lackone.add(t[:i]+t[i+1:])

def solver(x):
    if x in lackone:
        return True
    nowlen = len(x)
    if nowlen == tlen:
        miss = 0
        for i in range(nowlen):
            if t[i] != x[i]:
                miss += 1
        if miss <= 1:
            return True
        else:
            return False
    elif nowlen-1 == tlen:
        pre = ""
        for i in range(tlen()):
            if x[i] == t[i]:
                pre += t[i]
            else:
                break
        suf = ""
    else:
        return False

ans = []
ansbool = []
for i in range(1,n+1):
    s = input()
    ansbool.append(solver(s))
    if solver(s):
        ans.append(i)
ans.sort()
print(ans)
print(*ansbool,sep="\n")
print(len(ans))
print(*ans)