h,w = map(int,input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        flag = True
        for k in range(h):
            for m in range(w):
                flag &= a[(i+k)%h][(j+m)%w] == b[k][m]
        if flag:
            print("Yes")
            exit()
print("No")