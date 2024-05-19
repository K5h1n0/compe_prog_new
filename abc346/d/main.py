import sys
sys.setrecursionlimit(10**6)
n = 100
ans = []
def f(nows, flg):
    if len(nows) == n:
        if flg:
            ans.append(nows)
        return
    
    if nows[-1] == "0":
        f(nows+"1",flg)
        if not flg:
            f(nows+"0",True)
    else:
        f(nows+"0",flg)
        if not flg:
            f(nows+"1",True)

f("0", False)
f("1", False)
print(*ans,sep="\n")
