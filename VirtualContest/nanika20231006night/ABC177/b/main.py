s = input()
t = input()
ans = 10**10
for i in range(len(s)-len(t)+1):
    now = 0
    for j in range(len(t)):
        if s[i+j] != t[j]:
            now += 1
    ans = min(ans,now)
print(ans)