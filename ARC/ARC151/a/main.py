#解説AC
n = int(input())
s = input()
t = input()
cnt = 0
for i in range(n):
    if s[i] != t[i]:
        cnt += 1
if cnt % 2 == 1:
    print(-1)
    exit()
ans = list("1"*n)
scnt = cnt//2
tcnt = cnt//2
for i in range(n):
    if s[i] == t[i]:
        ans[i] = "0"
    else:
        if s[i] == "0" and 0 < scnt:
            ans[i] = "0"
            scnt -= 1
        elif t[i] == "0" and 0 < tcnt:
            ans[i] = "0"
            tcnt -= 1
print("".join(ans))