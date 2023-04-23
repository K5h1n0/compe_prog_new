n = int(input())
l = []
def f(x,moji):
    if x == 0:
        l.append(moji)
        return
    else:
        for i in range(3):
            f(x-1,moji+chr(ord("a")+i))

f(n,"")
l.sort()
print(*l,sep="\n")