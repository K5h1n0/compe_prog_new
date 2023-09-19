import itertools

n, k = map(int, input().split())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))
ans = []
for v in itertools.permutations(range(1, n), n-1):
    tmp = 0
    for i in range(len(v)):
        if i == 0:
            tmp += t[0][v[0]]
            continue
        tmp += t[v[i-1]][v[i]]
    tmp += t[v[-1]][0]
    ans.append(tmp)
cnt = 0
for i in ans:
    if i == k:
        cnt += 1
print(cnt)
