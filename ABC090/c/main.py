l = list(map(int,input().split()))
ans = 0
if l[0] == 2 or l[1] == 2:
    ans = 0
elif l[0] == 1 or l[1] == 1:
    l.remove(1)
    if sum(l) == 1:
        ans = 1
    else:
        ans = sum(l) - 2
else:
    ans = l[0]*l[1] - l[0]*2 - l[1]*2 + 4
print(ans)