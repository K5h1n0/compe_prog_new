# 解説AC

import sys
import copy
sys.setrecursionlimit(10**6)

def dfs(pre:int,num_list:list):
    if len(num_list) == n:
        ans.append(num_list)
        return
    for i in range(pre+1,m+1):
        nxt_num = copy.copy(num_list)
        nxt_num.append(i)
        dfs(i,nxt_num)

n,m = map(int,input().split())
ans = []
dfs(0,[])

for i in ans:
    print(*i)