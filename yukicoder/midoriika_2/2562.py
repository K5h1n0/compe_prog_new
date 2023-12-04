import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(array,visited,nowl):
    global ansset,length
    if len(nowl) == length:
        ansset.add("".join(nowl))
        return
    
    for i in range(length):
        visited[i] = True
        nowl.append(array[i])
        dfs(array,visited,nowl)
        visited[i] = False
            
    
ans = []
for _ in range(t):
    m = int(input())
    d = list(map(int,input().split()))
    l = []
    for i in range(len(d)):
        l += [str(i+1)]*d[i]
    length = len(l)
    ansset = set()
    dfs(l,[False]*length,[])
    print(ansset)
    if len(l) == 0:
        ans.append(0)
print(ans)