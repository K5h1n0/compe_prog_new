n,k = map(int,input().split())
s = list(input())
ans = ""
for i in range(n):
    if s[i] == "o" and k > 0:
        ans += "o"
        k -= 1
    else:
        ans += "x"
print(ans)