from collections import deque

n = int(input())
ans = []
stack = deque()
for i in range(n):
    l = list(input().split())
    if l[0] == "1":
        stack.append(l[1])
    elif l[0] == "2":
        ans.append(stack[-1])
    elif l[0] == "3":
        stack.pop()
print(*ans,sep="\n")