from collections import defaultdict

n,m = map(int,input().split())
a = list(map(int,input().split()))
score = []
d = defaultdict(list)
for i in range(1,n+1):
    inp = list(input())
    nowscore = 0
    for j in range(m):
        if inp[j] == "o":
            nowscore += a[j]
        else:
            #解けてない問題
            d[i].append((a[j]))
    score.append(nowscore+i)

othermax = []
for i in range(n):
    now = 0
    for j in range(n):
        if i == j:
            continue
        now = max(now,score[j])
    othermax.append(now)
for i in d:
    d[i].sort(reverse=True)
#print(d)
#print(score)
#print(othermax)

ans = [0]*n
for i in range(n):
    if othermax[i] < score[i]:
        continue
    addscore = 0
    cnt = 0
    for j in d[i+1]:
        addscore += j
        cnt += 1
        if othermax[i] < score[i] + addscore:
            ans[i] = cnt
            break
print(*ans,sep="\n")