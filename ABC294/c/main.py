n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
length = len(a) + len(b)
i = 0
j = 0
cnt = 1
ansa = []
ansb = []
while True:
    if i == len(a) and j == len(b):
        break
    if i < len(a):
        indexa = a[i]
    else:
        indexa = 999999999999
    if j < len(b):
        indexb = b[j]
    else:
        indexb = 999999999999
    if indexa < indexb:
        if i == len(a):
            pass
        else:
            ansa.append(cnt)
            i += 1
            cnt += 1
    if indexa > indexb:
        if b == len(b):
            pass
        else:
            ansb.append(cnt)
            j += 1
            cnt += 1
print(*ansa)
print(*ansb)