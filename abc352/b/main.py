s = input()
t = input()
idx = 0
ans = []
for i in range(len(t)):
    if s[idx] == t[i]:
        idx += 1
        ans.append(i+1)
print(*ans)