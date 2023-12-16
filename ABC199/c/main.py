n = int(input())
s = list(input())
q = int(input())
flg = True
for _ in range(q):
    t,a,b = map(int,input().split())
    a -= 1
    b -= 1
    if t == 1:
        if not flg:
            if n <= a:
                a -= n
            else:
                a += n
            if n <= b:
                b -= n
            else:
                b += n
        s[a],s[b] = s[b],s[a]
    elif t == 2:
        flg = not flg
if not flg:
    s[:n],s[n:] = s[n:],s[:n]
print("".join(s))