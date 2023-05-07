h,w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(input()))
b = []
for i in range(h):
    b.append(list(input()))
for i in range(h):
    for j in range(w):
        ans = "Yes"
        for k in range(h):
            for m in range(w):
                nowy = (i+k)%h
                nowx = (j+m)%w
                if a[k][m] != b[nowy][nowx]:
                    ans = "No"
                    break
            else:
                continue
            break
        if ans == "Yes":
            print(ans)
            exit()
print("No")