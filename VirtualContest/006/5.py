n = int(input())
l = []
for i in range(n):
    s,t = input().split()
    l.append([s,int(t)])
ans = 0
now = 0
s = set()
for i in range(len(l)):
    if l[i][0] not in s:
        s.add(l[i][0])
        if now < l[i][1]:
            now = l[i][1]
            ans = i
print(ans+1)