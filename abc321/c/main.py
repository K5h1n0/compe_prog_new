n = int(input())
l = []

def f(moji,nownum,remain):
    global l
    if remain == 0:
        l.append(int(moji))
        return
    for i in range(nownum-1,-1,-1):
        f(moji+str(i),i,remain-1)
f("",10,1)
f("",10,2)
f("",10,3)
f("",10,4)
f("",10,5)
f("",10,6)
f("",10,7)
f("",10,8)
f("",10,9)
l.append(9876543210)
l.sort()
l = l[1:]
print(l[n-1])