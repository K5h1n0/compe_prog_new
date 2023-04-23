h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
ans = []
for i in range(h):
    tmp = ""
    for j in range(w):
        if a[i][j] == 0:
            tmp += "."
        else:
            tmp += chr(ord("A") - 1 + a[i][j])
    ans.append(tmp)
print(*ans,sep="\n")