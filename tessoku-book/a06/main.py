n,q = map(int,input().split())
a = list(map(int,input().split()))
list_cumulative = [0]
total = 0
for i in range(len(a)):
    total += a[i]
    list_cumulative.append(total)
list_day = []
for i in range(q):
    l,r = map(int,input().split())
    list_day.append(list_cumulative[r]-list_cumulative[l-1])
print(*list_day,sep="\n")