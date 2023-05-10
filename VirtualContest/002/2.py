l = list(map(int,input().split()))
ans = ""
for i in range(len(l)):
    ans += chr(ord("a")-1+l[i])
print(ans)