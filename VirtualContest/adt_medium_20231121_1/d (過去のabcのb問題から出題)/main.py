h,w = map(int,input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        flg = True
        for k in range(h):
            for m in range(w):
                flg &= a[(i+k)%h][(j+m)%w] == b[k][m]
        if flg:
            print("Yes")
            exit()
print("No")