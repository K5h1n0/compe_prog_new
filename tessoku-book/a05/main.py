n,k = map(int,input().split())
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        l = k - i - j
        if 0 < l <= n:
            cnt += 1
print(cnt)

#ほぼ解説ACみたいなもの。ちょっと苦手。forループを3回回してはダメ。