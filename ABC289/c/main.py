n,m = map(int,input().split())
l = []
for i in range(m):
    c = int(input())
    l.append(list(map(int,input().split())))
cnt = 0
for i in range(2 ** m):
    tmp = []
    for j in range(m):
        if ((i >> j) & 1):
            tmp+=l[j]
    if len(set(tmp)) == n:
        cnt += 1
print(cnt)