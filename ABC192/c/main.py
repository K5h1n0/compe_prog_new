n,k = map(int,input().split())
if k == 0:
    print(n)
    exit()
s1 = sorted(list(str(n)),reverse=True)
s2 = sorted(s1[:])
now = int("".join(s1))-int("".join(s2))
for _ in range(k-1):
    s1 = sorted(list(str(now)),reverse=True)
    s2 = sorted(s1[:])
    now = int("".join(s1))-int("".join(s2))
print(now)