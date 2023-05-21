import sys
sys.setrecursionlimit(10**6)

def dfs(next):
    if bo[next] != 1:
        bo[next] = 1
        dfs(a[next])

n,start = map(int,input().split())
a = [0] + list(map(int,input().split()))
bo = [0] * (n+1)
dfs(start)
bo[start] = 1
print(sum(bo))