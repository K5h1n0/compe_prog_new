a = list("ooxooxoxox")
b = list("xoooxooxoo")
c = list("xoxooxxxxo")

for i in range(2**10):
    l = []
    aa = 5
    ba = 6
    ca = 5
    for j in range(10):
        if ((i >> j) & 1):
            l.append(j)
    ans = list("o"*10)
    for j in range(len(l)):
        ans[l[j]] = "x"
    
    for j in range(len(ans)):
        if ans[j] == a[j]:
            aa -= 1
        if ans[j] == b[j]:
            ba -= 1
        if ans[j] == c[j]:
            ca -= 1
    if aa == 0 and ba == 0 and ca == 0:
        print(ans)
    