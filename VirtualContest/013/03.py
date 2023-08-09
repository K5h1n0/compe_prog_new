n,m = map(int,input().split())
s = list(input().split())
t = set(input().split())
for i in range(len(s)):
    if s[i] in t:
        print("Yes")
    else:
        print("No")