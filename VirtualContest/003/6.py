n = int(input())
p = list(map(int,input().split()))
nowi = p[-1]
l = []
l.append(nowi)
for i in range(n-2,-1,-1):
    if p[i] < nowi:
        nowi = p[i]
        l.append(p[i])
    else:
        koukan = p[i]
        index = i
        break
pre = 0
for i in range(len(l)):
    if l[i] < koukan:
        pre = max(pre,l[i])
l.remove(pre)
l.append(koukan)
p = p[:index] + [pre] + sorted(l,reverse=True)
print(*p)