n = int(input())
h = list(map(int,input().split()))
l = []
l.append(0)
for i in range(1,n):
    if i == 1: #1つ目の足場から2つ目の足場に移る時は、2つ前の足場が存在しないので、このような処理になる。
        l.append(abs(h[0]-h[i]))
        continue
    l.append(min(l[i-1]+abs(h[i]-h[i-1]),l[i-2]+abs(h[i]-h[i-2])))
print(l[-1])