from collections import deque

n = int(input())
s = input()
stack = deque()
b = [0]*n
cnt = 1
length = 0
for i in range(n):
    if s[i] == "(":
        stack.append(i)
        length += 1
    elif s[i] == ")" and 1 <= length:
        b[stack.pop()],b[i] = cnt,cnt
        cnt += 1
        length -= 1
flg = 0
for i in range(n):
    if b[i] != 0 and flg == 0:
        flg = max(flg,b[i])
    elif flg == b[i]:
        flg = 0
    elif flg != 0:
        b[i] = flg
ans = [s[i] for i in range(n) if b[i] == 0]
print(*ans,sep="")