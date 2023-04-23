n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
print(a,"\n",b)
ai = 0
bi = 0
minimum = 99999999
while True:
    if n <= ai and m <= bi:
        break
    if ai < n and a[ai] <= b[bi]:
        ai += 1
    elif bi < m and a[ai] > b[bi]:
        bi += 1
    if ai < n and bi < m:
        minimum = min(abs(a[ai]-b[bi]),minimum)
    print(minimum)
print("終了")
print(minimum)