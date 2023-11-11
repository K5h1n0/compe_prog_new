n,k = map(int,input().split())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

ans = set()

def dfs(xor,remain):
    global ans
    if remain == n:
        ans.add(xor)
        return
    for i in range(k):
        dfs(xor^l[remain][i],remain+1)

dfs(0,0)
print("Found" if 0 in ans else "Nothing")