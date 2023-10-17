n = int(input())
s = input()
l = [0]*(n+1)
for i in range(n):
    if s[i] == "(":
        l[i] += 1
    elif s[i] == ")":
        l[i+1] -= 1
print(l)
for i in range(1,len(l)):
    l[i] += l[i-1]
print(l)
ans = ""
for i in range(len(l)-1):
    if l[i] == 0:
        ans += s[i]
print(ans)