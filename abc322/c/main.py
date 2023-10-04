n, m = map(int, input().split())
a = list(map(int, input().split()))
seta = set(a[:])
ans = []
nowcnt = 0
for i in range(n, 0, -1):
    if i in seta:
        nowcnt = 0
    else:
        nowcnt += 1
    ans.append(nowcnt)
ans.reverse()
print(*ans, sep="\n")
