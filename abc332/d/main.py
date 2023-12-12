import time
h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
b = [list(map(int,input().split())) for _ in range(h)]

def f():
    i1,j1,i2,j2 = -1,-1,-1,-1
    for i in range(h):
        for j in range(w):
            if a[i][j] != b[i][j]:
                i1 = i
                j1 = j
                tmp = a[i][j]
                break
        else:
            continue
        break
    for i in range(h):
        for j in range(w):
            if b[i][j] == tmp:
                i2 = i
                j2 = j
                break
        else:
            continue
        break
    return i1,j1,i2,j2

def changerow(i1,i2):
    b[i1],b[i2] = b[i2],b[i1]

def changecolumn(j1,j2):
    for i in b:
        i[j1],i[j2] = i[j2],i[j1]

cnt = 0
for i in range(10):
    o,p,q,r = f()
    if o == p and q == r and p == q:
        break
    elif o != q:
        changerow(o,p)
        cnt += 1
    elif p != r:
        changecolumn(p,r)
        cnt += 1
    print(*b,sep="\n")
    print()
    print()
    time.sleep(0.1)
print(cnt)
