import bisect 

n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
c = sorted(list(set(a+b)))
sell = [0] * len(c)
buy = [0] * len(c)
#print(c)
#print(sell)
#print(buy)
for i in range(len(a)-1,-1,-1):
    sell[bisect.bisect_left(c,a[i])-1] -= 1
for i in range(len(b)-1,-1,-1):
    buy[bisect.bisect_left(c,b[i])] += 1
tmp = len(a)
for i in range(len(sell)-1,-1,-1):
    tmp += sell[i]
    sell[i] = tmp
tmp = 0
for i in range(len(buy)-1,-1,-1):
    tmp += buy[i]
    buy[i] = tmp
#print(sell)
#print(buy)
for i in range(len(sell)):
    if sell[i] >= buy[i]:
        if buy[i] == 0:
            print(c[i-1]+1)
        else:
            print(c[i])
        exit()