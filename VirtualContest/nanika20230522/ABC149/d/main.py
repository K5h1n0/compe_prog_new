n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()
l = [0]*len(t)
ans = 0
for i in range(len(t)):
    if t[i] == "r":
        ans += p
    elif t[i] == "s":
        ans += r
    elif t[i] == "p":
        ans += s
print(ans)