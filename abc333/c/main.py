import sys

sys.setrecursionlimit(10**6)

n = int(input())
r = []
for i in range(1,13):
    r.append(int("1"*i))
ans = []

def f(array,cnt):
    if cnt == 3:
        ans.append(sum(array))
        return
    for i in range(len(r)):
        f(array+[r[i]],cnt+1)

f([],0)
ans = sorted(list(set(ans)))
print(ans[n-1])